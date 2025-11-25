import os
import shutil
import pandas as pd
import re
from pathlib import Path

def clean_user_folder_name(folder_name):
    """Extracts 'userX' from folder names like '用户8-土汉' or '用户30-明芯'"""
    try:
        folder_name = str(folder_name)
        # Handle Chinese "用户" prefix with optional suffix after number
        match = re.search(r"(用户|user)\s*(\d+)", folder_name, re.IGNORECASE)
        if match:
            return f"user{match.group(2)}"
        return None
    except:
        return None

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
    """Extract frame number from filename like Color_00000170.png"""
    try:
        filename = os.path.basename(str(filename))
        filename_clean = str(filename).replace("\"", "")
        match = re.search(r'(\d+)\_Color.png$', filename_clean, re.IGNORECASE)
        return int(match.group(1)) if match else None
    except:
        return None

def extract_user_name(full_path):
    try:
        full_path = str(full_path).replace('\\', '/')
        match = re.search(r'(用户\d+)', full_path, re.IGNORECASE)
        if match:
            return clean_user_folder_name(match.group(0))
        return None
    except:
        return None

def extract_scene_number(full_path):
    """
    Extract scene number like '7-2-3' from a path ending in .../7/7-2/7-2-3/<filename>
    """
    try:
        full_path = str(full_path).replace('\\', '/')
        match = re.search(r'(\d+-\d+-\d+)(?=/[^/]*$|$)', full_path)
        return match.group(1) if match else None
    except:
        return None

def process_labels_from_excel():
    # Path configurations
    input_excel = 'Combined_Data.xlsx'  # Single Excel file with all labels
    lm_base = 'LM_data/RGB'      # Source frames directory
    output_base = 'SM_data/RGB_final'  # Output directory
    
    print(f"Starting processing...")
    print(f"Reading labels from: {os.path.abspath(input_excel)}")
    print(f"Looking for source frames in: {os.path.abspath(lm_base)}")
    print(f"Output will go to: {os.path.abspath(output_base)}")
    
    os.makedirs(output_base, exist_ok=True)
    
    if not os.path.exists(input_excel):
        print(f"ERROR: File not found - {input_excel}")
        return
    
    try:
        # Read the Excel file
        df = pd.read_excel(input_excel)
        df.columns = [col.strip().lower() for col in df.columns]
        
        # Validate required columns
        if not all(col in df.columns for col in ['path', 'begin', 'end', 'label']):
            print("Missing required columns in Excel file. Need: path, begin, end, label")
            return
            
        print(f"Found {len(df)} entries in {input_excel}")
    except Exception as e:
        print(f"Error reading {input_excel}: {e}")
        return
    
    # Process each row
    for i, row in df.iterrows():
        try:
            # Extract information from the path
            user_name = extract_user_name(row['path'])
            scene_number = extract_scene_number(row['path'])
            
            if not user_name or not scene_number:
                print(f"Could not extract user or scene from path: {row['path']}")
                continue
                
            # Get frame numbers
            begin_frame = extract_frame_number(row['begin'])
            end_frame = extract_frame_number(row['end'])
            
            if begin_frame is None or end_frame is None:
                print(f"Invalid frame numbers in row {i}")
                continue
                
            # Create output directory structure: label/user_name/scene_number
            output_dir = os.path.join(output_base, str(row['label']), user_name, scene_number)
            os.makedirs(output_dir, exist_ok=True)
            
            # Construct source directory path from the user_name and scene_number
            source_dir = os.path.join(lm_base, user_name, scene_number)
            
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
    process_labels_from_excel()
    print("\nProcessing complete!")