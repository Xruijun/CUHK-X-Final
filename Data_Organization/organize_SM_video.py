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
mapping_df = pd.read_excel("action_translation_revised.xlsx")  # contains Chinese + English mapping
video_df = pd.read_excel("Color_logic_video.xlsx")  # contains video_path, logic, candidate

# Try to detect which columns are which (you can adjust manually if needed)
print("Mapping columns:", mapping_df.columns)

# Suppose mapping_df columns are: [number, Chinese_action, English_action]
# Build two dictionaries:
#   logic_to_number: English action → number
#   number_to_chinese: number → Chinese action
logic_to_number = pd.Series(mapping_df.iloc[:, 0].values, index=mapping_df.iloc[:, 2].str.strip()).to_dict()
number_to_chinese = pd.Series(mapping_df.iloc[:, 1].values, index=mapping_df.iloc[:, 0].values).to_dict()

# Base folder
base_folder = "SM_data/RGB"

# Store results
results = []

# Iterate through each video row
for idx, row in video_df.iterrows():
    logic_name = row["logic"].strip()
    video_path = row["video_path"]

    # --- Find corresponding number from mapping ---
    number = logic_to_number.get(logic_name)
    if number is None:
        print(f"⚠️ Logic not found in mapping: {logic_name}")
        continue

    chinese_action = number_to_chinese.get(number, "未知动作")

    # --- Find folder that starts with that number ---
    rgb_folders = [f for f in os.listdir(base_folder) if f.startswith(str(number))]
    if not rgb_folders:
        print(f"❌ No folder found starting with {number} for logic '{logic_name}'")
        continue

    rgb_folder = os.path.join(base_folder, rgb_folders[0])

    # --- Extract and clean user folder name ---
    parts = video_path.split("/")
    if len(parts) < 6:
        print(f"⚠️ Unexpected video_path format: {video_path}")
        continue

    raw_user_folder = parts[2]  # e.g. 用户1-丹妮
    cleaned_user = clean_user_folder_name(raw_user_folder)
    if not cleaned_user:
        print(f"⚠️ Could not clean folder name: {raw_user_folder}")
        continue

    subfolder = parts[4]  # e.g. "1-1-1"

    # --- Construct final path (Chinese action retained) ---
    final_folder_name = f"{number}_{chinese_action}"
    target_path = os.path.join("SM_video", "RGB", final_folder_name, cleaned_user, subfolder, "RGB.mp4")

    results.append({
        "logic_en": logic_name,
        "logic_cn": chinese_action,
        "video_path": video_path,
        "mapped_number": number,
        "final_path": target_path
    })

# --- Save results to CSV ---
output_folder = "SM_video"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "final_video_paths.csv")

pd.DataFrame(results).to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"\n✅ Saved {len(results)} paths to: {output_path}")
