import shutil
from pathlib import Path
import re

def clean_user_folder_name(folder_name):
    """Extracts 'userX' from folder names like '用户8-土汉'"""
    match = re.search(r"(用户|user)(\d+)", str(folder_name), re.IGNORECASE)
    return f"user{match.group(2)}" if match else None

def clean_action_folder_name(folder_name):
    """Removes hyphen and anything after it in action folder names"""
    return str(folder_name).replace("-", "")

# Define input/output roots
src_root = Path("labels/SM")
dst_root = Path("SM_data/Thermal")

# Traverse recursively
for thermal_dir in src_root.rglob("thermal"):
    if thermal_dir.is_dir():
        # Example: labels/SM/action/user/1/1-1/1-1-1/thermal
        parts = thermal_dir.parts

        # Extract action and user
        try:
            action = parts[2]  # after labels/SM
            user = parts[3]
            last_folder = parts[6]  # "1-1-1"
        except IndexError:
            print(f"Skipping {thermal_dir}, unexpected path format")
            continue

        # Destination path
        clean_user = clean_user_folder_name(user)
        clean_action = clean_action_folder_name(action)
        dst_path = dst_root / clean_action / clean_user / last_folder
        dst_path.mkdir(parents=True, exist_ok=True)

        # Copy contents of thermal folder
        for item in thermal_dir.iterdir():
            if item.is_file():
                shutil.copy2(item, dst_path / item.name)
            elif item.is_dir():
                shutil.copytree(item, dst_path / item.name, dirs_exist_ok=True)

        print(f"Copied from {thermal_dir} → {dst_path}")
