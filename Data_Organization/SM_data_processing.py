import os
import shutil
import pandas as pd
import re
from pathlib import Path

def extract_frame_number(filename):
    """Extract frame number from filename like Color_00000170.jpg"""
    try:
        filename = os.path.basename(str(filename))
        filename_clean = str(filename).replace("\"", "")
        match = re.search(r'(\d+)\.jpg$', filename_clean, re.IGNORECASE)
        return int(match.group(1)) if match else None
    except:
        return None

def extract_frame_number_png(filename):
    """Extract frame number from filename like Color_00000170.jpg"""
    try:
        filename = os.path.basename(str(filename))
        filename_clean = str(filename).replace("\"", "")
        match = re.search(r'(\d+)\_Color.png$', filename_clean, re.IGNORECASE)
        return int(match.group(1)) if match else None
    except:
        return None

def clean_user_folder_name(folder_name):
    """Extracts 'userX' from folder names like '用户8-土汉'"""
    match = re.search(r"(用户|user)(\d+)", str(folder_name), re.IGNORECASE)
    return f"user{match.group(2)}" if match else None

def clean_action_folder_name(folder_name):
    """Removes hyphen and anything after it in action folder names"""
    return str(folder_name).replace("-", "")

def extract_scene_path(full_path):
    """Extract the scene path (like 5-1-1) from the full path"""
    try:
        full_path = str(full_path).replace('\\', '/')
        # Look for pattern like /5/5-1/5-1-1/ or \5\5-1\5-1-1\
        match = re.search(r'/(\d+)/(\d+-\d+)/(\d+-\d+-\d+)/', full_path)
        if match:
            return match.group(3)  # Returns the 5-1-1 part
        return None
    except:
        return None

def process_labels_folder():
    # Base paths
    labels_base = 'labels/SM'
    lm_base = 'LM_data/RGB'
    output_base = 'SM_data/RGB_final'
    
    print(f"Starting processing...")
    print(f"Looking for labels in: {os.path.abspath(labels_base)}")
    print(f"Looking for source frames in: {os.path.abspath(lm_base)}")
    print(f"Output will go to: {os.path.abspath(output_base)}")
    
    os.makedirs(output_base, exist_ok=True)
    
    if not os.path.exists(labels_base):
        print(f"ERROR: Directory not found - {labels_base}")
        return
    
    # Iterate through action folders
    for action_folder in os.listdir(labels_base):
        full_action_path = os.path.join(labels_base, action_folder)
        if not os.path.isdir(full_action_path):
            continue
            
        print(f"\nProcessing action folder: {action_folder}")
        
        # Clean the action folder name for output
        clean_action = clean_action_folder_name(action_folder)
        
        # Iterate through user folders
        for user_folder in os.listdir(full_action_path):
            if not re.match(r'用户\d+', user_folder):
                continue
                
            full_user_path = os.path.join(full_action_path, user_folder)
            if not os.path.isdir(full_user_path):
                continue
                
            print(f"\nProcessing user folder: {user_folder}")
            labels_file = os.path.join(full_user_path, 'labels.xlsx')
            
            if not os.path.exists(labels_file):
                print(f"Labels file not found: {labels_file}")
                continue
                
            try:
                df = pd.read_excel(labels_file)
                df.columns = [col.strip().lower() for col in df.columns]
                
                if not all(col in df.columns for col in ['path', 'begin', 'end']):
                    print(f"Missing required columns in {labels_file}")
                    continue
                    
                print(f"Found {len(df)} entries in {labels_file}")
            except Exception as e:
                print(f"Error reading {labels_file}: {e}")
                continue
                
            # Process each row
            for i, row in df.iterrows():
                try:
                    scene_path = extract_scene_path(row['path'])
                    if not scene_path:
                        print(f"Could not extract scene path from: {row['path']}")
                        continue
                    
                    print(f"Using scene path: {scene_path}")
                    
                    begin_frame = extract_frame_number(row['begin'])
                    end_frame = extract_frame_number(row['end'])
                    
                    if begin_frame is None or end_frame is None:
                        print(f"Invalid frame numbers in row {i}")
                        continue
                    
                    user_folder_updated = clean_user_folder_name(user_folder)
                    if not user_folder_updated:
                        print(f"Could not parse user number from {user_folder}")
                        continue
                        
                    # Use the cleaned action folder name here
                    output_dir = os.path.join(output_base, clean_action, user_folder_updated, scene_path)
                    os.makedirs(output_dir, exist_ok=True)
                    
                    source_dir = os.path.join(lm_base, user_folder_updated, scene_path)
                    
                    if not os.path.exists(source_dir):
                        print(f"Source directory not found: {source_dir}")
                        continue
                    
                    # Copy matching frames
                    copied_count = 0
                    for frame_file in os.listdir(source_dir):
                        if not frame_file.lower().startswith('color'):
                            continue
                            
                        frame_num = extract_frame_number(frame_file)
                        if frame_num is None:
                            continue
                            
                        if begin_frame <= frame_num <= end_frame:
                            src = os.path.join(source_dir, frame_file)
                            dst = os.path.join(output_dir, frame_file)
                            shutil.copy2(src, dst)
                            copied_count += 1
                    
                    print(f"Copied {copied_count} frames ({begin_frame}-{end_frame}) to {output_dir}")
                            
                except Exception as e:
                    print(f"Error processing row {i}: {e}")
                    continue

if __name__ == '__main__':
    process_labels_folder()
    print("\nProcessing complete!")