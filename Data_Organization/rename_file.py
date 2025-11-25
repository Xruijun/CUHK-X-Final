import re
from pathlib import Path
import logging
from datetime import datetime, timedelta
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nyx_rename.log'),
        logging.StreamHandler()
    ]
)

def parse_folder_timestamp(folder_name: str) -> datetime:
    """Extract timestamp from NYX folder name"""
    match = re.match(
        r'NYX650_(\d{4})_(\d{2})_(\d{2})_(\d{2})_(\d{2})_(\d{2})_(\d{3})',
        folder_name
    )
    if not match:
        raise ValueError(f"Invalid folder name format: {folder_name}")
    
    return datetime.strptime(
        f"{match.group(1)}-{match.group(2)}-{match.group(3)} "
        f"{match.group(4)}:{match.group(5)}:{match.group(6)}.{match.group(7)}",
        '%Y-%m-%d %H:%M:%S.%f'
    )

def process_nyx_folder(nyx_dir: Path):
    """Process a single NYX folder"""
    try:
        # Get base timestamp from folder name
        base_timestamp = parse_folder_timestamp(nyx_dir.name)
        logging.info(f"Processing {nyx_dir} with base timestamp {base_timestamp}")
        
        rename_log = []
        
        # Process all image files
        for file in nyx_dir.glob('*'):
            if file.suffix.lower() not in ('.jpg', '.jpeg', '.png'):
                continue
            
            try:
                # Extract frame number from filename (e.g., Color_00000033.jpg)
                if not (match := re.fullmatch(r'^Color_(\d+)\.(jpg|jpeg|png)$', file.name, re.IGNORECASE)):
                    logging.warning(f"Skipping non-conforming file: {file.name}")
                    continue
                
                frame_num = int(match.group(1))
                
                # Calculate timestamp (100ms intervals from base)
                file_timestamp = base_timestamp + timedelta(milliseconds=100 * (frame_num - 1))
                timestamp_str = file_timestamp.strftime('%Y-%m-%d_%H-%M-%S.%f')[:-3]
                
                # Build new filename
                new_name = f"Color_{timestamp_str}_{frame_num:08d}{file.suffix.lower()}"
                new_path = file.with_name(new_name)
                
                # Rename the file
                if new_path.exists():
                    logging.warning(f"File exists, skipping: {new_path}")
                    status = 'skipped (exists)'
                else:
                    file.rename(new_path)
                    status = 'renamed'
                    logging.info(f"Renamed: {file.name} → {new_name}")
                
                rename_log.append({
                    'original': file.name,
                    'new': new_name,
                    'status': status
                })
                
            except Exception as e:
                logging.error(f"Error processing {file.name}: {e}")
                rename_log.append({
                    'original': file.name,
                    'new': '',
                    'status': f'error: {str(e)}'
                })
        
        # Save rename log
        if rename_log:
            log_path = nyx_dir.parent / f"nyx_rename_log_{nyx_dir.name}.csv"
            pd.DataFrame(rename_log).to_csv(log_path, index=False)
            logging.info(f"Saved rename log to {log_path}")
            
    except Exception as e:
        logging.error(f"Failed processing {nyx_dir}: {e}")

def find_nyx_folders(base_dir: Path):
    """Find all NYX folders in the structure"""
    # Match patterns like: */after_preprocess_2/NYX650_*
    # Handles any number structure (1/1-1/1-1-1, 2/2-1/2-1-3, etc.)
    return [
        folder for folder in base_dir.glob("*/*/*/*/after_preprocess_2/NYX650_*")
        if folder.is_dir()
    ]

def main():
    base_dir = Path("data/redo_data")
    if not base_dir.exists():
        logging.error(f"Base directory not found: {base_dir}")
        return
    
    nyx_folders = find_nyx_folders(base_dir)
    if not nyx_folders:
        logging.error("No NYX folders found in the expected structure")
        return
    
    logging.info(f"Found {len(nyx_folders)} NYX folders to process")
    
    for folder in nyx_folders:
        process_nyx_folder(folder)
    
    logging.info("Processing complete!")

if __name__ == "__main__":
    main()