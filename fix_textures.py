import os
import json
import re

TEXTURE_DIR = "textures"
JSON_FILE = "textures.json"

def clean_name(name):
    name = name.lower()
    name = name.replace(" ", "_")
    name = re.sub(r"[^a-z0-9._-]", "", name)
    return name

# Rename files
for filename in os.listdir(TEXTURE_DIR):
    old_path = os.path.join(TEXTURE_DIR, filename)
    if os.path.isfile(old_path):
        new_name = clean_name(filename)
        new_path = os.path.join(TEXTURE_DIR, new_name)

        if filename != new_name:
            print(f"Renaming: {filename} -> {new_name}")
            os.rename(old_path, new_path)

# Fix JSON
with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for tex in data["textures"]:
    if "url" in tex:
        filename = tex["url"].split("/")[-1]
        tex["url"] = f"{TEXTURE_DIR}/{clean_name(filename)}"

with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ All textures fixed for GitHub Pages!")
