from pathlib import Path
import shutil
import re

def clean_user_folder_name(folder_name):
    """Extracts 'userX' from folder names like '用户1-fh', 'user2-dfj', etc."""
    match = re.search(r"(用户|user)(\d+)", folder_name, re.IGNORECASE)
    if match:
        return f"user{match.group(2)}"  # Returns "user1", "user2", etc.
    return None  # If no number found

def normalize_parentheses(filename):
    """Replaces full-width parentheses with half-width parentheses in filenames"""
    return filename.replace("（", "(").replace("）", ")")

def organize_up_down_images(data_root: Path, output_root: Path):
    """
    Process folders to organize files that start with '上' or '下' into new structure,
    while normalizing parentheses in filenames.
    """
    for user_folder in data_root.iterdir():
        if not user_folder.is_dir() or not user_folder.name.startswith("用户"):
            continue

        user_num = clean_user_folder_name(user_folder.name)
        if not user_num:
            continue
        
        print(f"\nProcessing user: {user_num}")

        # Enter session level
        for session in user_folder.iterdir():
            if not session.is_dir():
                print(f"Skipping non-directory: {session}")
                continue

            # Enter segment group level
            for segment_group in session.iterdir():
                if not segment_group.is_dir():
                    continue

                # Enter segment level
                for segment in segment_group.iterdir():
                    if not segment.is_dir():
                        continue

                    after_path = segment / "after_preprocess_2"
                    if not after_path.exists():
                        continue

                    # Find all files starting with 上 or 下
                    up_down_files = (list(after_path.glob("上*")) + 
                                   list(after_path.glob("下*")))

                    if not up_down_files:
                        continue
                        
                    # Create target directory
                    target_dir = output_root / user_num / segment.name
                    target_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Copy files with normalized parentheses
                    for file in up_down_files:
                        new_name = normalize_parentheses(file.name)
                        target_path = target_dir / new_name
                        shutil.copy2(file, target_path)
                        print(f"Copied {file} to {target_path}")

# Example usage
organize_up_down_images(Path("data_2"), Path("LM_data/IMU"))