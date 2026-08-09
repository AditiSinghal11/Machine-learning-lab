# AI-assisted code generated using ChatGPT
# Experiment: Current working directory and files

from pathlib import Path

current_folder = Path.cwd()

print("Current Folder:")
print(current_folder)

print("\nFiles in this folder:")
for item in current_folder.iterdir():
    print(item.name)
