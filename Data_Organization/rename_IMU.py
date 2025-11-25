import os
import re
import shutil
import csv

def rename_time_column(csv_path):
    """Rename '时间' column to 'timeframe' in a CSV file"""
    try:
        # Read the original file
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = list(reader)
        
        # Rename the column if it exists
        if '时间' in header:
            header[header.index('时间')] = 'timeframe'
        
        # Write back to the file
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
            
    except Exception as e:
        print(f"Error processing {csv_path}: {str(e)}")

def copy_and_rename_imu_files(source_path, target_path):
    # Create the target directory if it doesn't exist
    os.makedirs(target_path, exist_ok=True)
    
    # Iterate through each user folder (user1 to user30)
    for user_num in range(1, 31):
        user_folder = f"user{user_num}"
        source_user_path = os.path.join(source_path, user_folder)
        target_user_path = os.path.join(target_path, user_folder)
        
        if not os.path.exists(source_user_path):
            continue
            
        # Create user folder in target if it doesn't exist
        os.makedirs(target_user_path, exist_ok=True)
        
        # Iterate through each scene folder (format X-Y-Z)
        for scene_folder in os.listdir(source_user_path):
            if not re.match(r'^\d+-\d+-\d+$', scene_folder):
                continue
                
            source_scene_path = os.path.join(source_user_path, scene_folder)
            target_scene_path = os.path.join(target_user_path, scene_folder)
            
            # Create scene folder in target if it doesn't exist
            os.makedirs(target_scene_path, exist_ok=True)
            
            # Process each CSV file in the source scene folder
            for filename in os.listdir(source_scene_path):
                source_file_path = os.path.join(source_scene_path, filename)
                
                if filename.startswith('上') and filename.endswith('.csv'):
                    # Copy and rename 上*.csv to upper(LA+RA+C).csv
                    target_filename = "upper(LA+RA+C).csv"
                    target_file_path = os.path.join(target_scene_path, target_filename)
                    shutil.copy2(source_file_path, target_file_path)
                    rename_time_column(target_file_path)
                    print(f"Processed: {os.path.join(user_folder, scene_folder, filename)} -> {target_filename}")
                
                elif filename.startswith('下') and filename.endswith('.csv'):
                    # Copy and rename 下*.csv to lower(LL+RL).csv
                    target_filename = "lower(LL+RL).csv"
                    target_file_path = os.path.join(target_scene_path, target_filename)
                    shutil.copy2(source_file_path, target_file_path)
                    rename_time_column(target_file_path)
                    print(f"Processed: {os.path.join(user_folder, scene_folder, filename)} -> {target_filename}")
                else:
                    # Copy other files as-is
                    target_file_path = os.path.join(target_scene_path, filename)
                    shutil.copy2(source_file_path, target_file_path)
                    if filename.endswith('.csv'):
                        rename_time_column(target_file_path)
                    print(f"Processed: {os.path.join(user_folder, scene_folder, filename)} (unchanged)")

if __name__ == "__main__":
    source_path = "LM_data/IMU"
    target_path = "LM_data/IMU2"
    
    try:
        copy_and_rename_imu_files(source_path, target_path)
        print("\nFile processing completed successfully!")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")