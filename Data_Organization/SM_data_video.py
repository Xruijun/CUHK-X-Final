import os
import re
import pandas as pd

def clean_user_folder_name(folder_name):
    """Extracts 'userX' from folder names like '用户1-fh', 'user2-dfj', etc."""
    match = re.search(r"(用户|user)(\d+)", folder_name, re.IGNORECASE)
    if match:
        return f"user{match.group(2)}"
    return None

# --- Load Excel files ---
mapping_df = pd.read_excel("action_translation_revised.xlsx")  # number + Chinese + English
video_df = pd.read_excel("video_data/video_logic/Color_logic_video.xlsx")  # video_path, logic, candidate

# Build mapping from logic name to number
# Assuming mapping_df columns: [number, Chinese_action, English_action]
logic_to_number = pd.Series(
    mapping_df.iloc[:, 0].values,  # number
    index=mapping_df.iloc[:, 1].str.strip()  # English logic
).to_dict()

# --- Path where the action folders are located ---
base_action_dir = "SM_video/RGB"

# Prepare list for updated paths
new_paths = []

# Iterate through each video row
for idx, row in video_df.iterrows():
    logic_name = str(row["logic"]).strip()
    video_path = str(row["video_path"])

    # --- Find corresponding number ---
    number = logic_to_number.get(logic_name)
    if number is None:
        print(f"⚠️ No mapping found for logic: {logic_name}")
        new_paths.append(video_path)
        continue

    # --- Find the actual folder starting with that number ---
    action_folder = None
    for folder_name in os.listdir(base_action_dir):
        if folder_name.startswith(str(number)):
            action_folder = folder_name
            break

    if action_folder is None:
        print(f"⚠️ No folder found for number {number} in {base_action_dir}")
        new_paths.append(video_path)
        continue

    parts = video_path.split("/")
    if len(parts) < 6:
        print(f"⚠️ Unexpected video_path format: {video_path}")
        new_paths.append(video_path)
        continue

    # --- Extract and clean user folder name ---
    raw_user_folder = parts[2]  # e.g. 用户1-丹妮
    cleaned_user = clean_user_folder_name(raw_user_folder)
    if not cleaned_user:
        print(f"⚠️ Could not clean folder name: {raw_user_folder}")
        new_paths.append(video_path)
        continue

    subfolder = parts[5]  # e.g. "1-1-1"

    # --- Construct new video path ---
    new_video_path = os.path.join(
        base_action_dir, action_folder, cleaned_user, subfolder, "RGB.mp4"
    ).replace("\\", "/")

    new_paths.append(new_video_path)

# --- Replace video_path column ---
video_df["video_path"] = new_paths

# --- Save updated CSV ---
output_csv = "RGB_logic.csv"
video_df.to_csv(output_csv, index=False, encoding="utf-8-sig")

print(f"\n✅ Updated CSV saved as: {output_csv}")
