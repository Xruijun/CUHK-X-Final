import pandas as pd
import shutil
from pathlib import Path
import re

def clean_user_folder_name(folder_name):
    """Extracts 'userX' from folder names like '用户1-fh', 'user2-dfj', etc."""
    match = re.search(r"(用户|user)(\d+)", folder_name, re.IGNORECASE)
    if match:
        return f"user{match.group(2)}"
    return None

def extract_frame_number(name):
    """Extract numeric frame index from names like 'frame_000389.jpg' or '389'."""
    if isinstance(name, str):
        digits = re.findall(r"\d+", name)
        if digits:
            return int(digits[-1])  # last number is frame index
    return int(name)

csv_path = Path("SM_thermal_16-30.csv")
data_root = Path("data_2")
output_root = Path("SM_data")

# Read CSV
df = pd.read_csv(csv_path)

for idx, row in df.iterrows():
    raw_path = str(row["path"]).replace('"', '').replace("\\", "/").strip()

    # Always keep last 4 parts of path (works for absolute + relative)
    parts = Path(raw_path).parts[-4:]
    if len(parts) < 4:
        print(f"[Skipped] Path has too few parts: {raw_path}")
        continue

    # Remove leading/trailing spaces from each component
    user, scene, subscene, level = [p.strip() for p in parts]
    begin_num = extract_frame_number(row["begin"])
    end_num = extract_frame_number(row["end"])

    if "用户" not in user:
        print(f"[Skipped] 用户 not found in path: {user}")
        continue

    # Build base_dir
    base_dir = data_root / Path(*parts) / "after_preprocess_2"

    # Find thermal folder
    thermal_folder = next(
        (f for f in base_dir.iterdir() if f.is_dir() and f.name.startswith("thermal")),
        None
    )

    if not thermal_folder:
        print(f"[Skipped] No folder starting with 'thermal' in: {base_dir}")
        continue

    # Collect images
    all_imgs = sorted(thermal_folder.glob("frame_*.jpg"))
    selected_imgs = [
        img for img in all_imgs
        if begin_num <= int(img.stem.split("_")[-1]) <= end_num
    ]

    if not selected_imgs:
        print(f"[Skipped] No frames in range: {begin_num} to {end_num}")
        continue

    # === Build destination folder ===
    clean_user = clean_user_folder_name(user)
    action = str(row["labels"]).strip()   # action from CSV column
    dest_dir = output_root / "Thermal" / action / clean_user / level
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Copy frames
    for img_path in selected_imgs:
        dest_path = dest_dir / img_path.name
        if not dest_path.exists():
            shutil.copy2(img_path, dest_path)

    print(f"[Copied] {len(selected_imgs)} frames to {dest_dir}")
