import cv2
import numpy as np
import os
from pathlib import Path

def imread_unicode(path):
    print(f"Reading file: {path}")
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return None
    data = np.fromfile(path, dtype=np.uint8)
    if data.size == 0:
        print(f"Empty data read from file: {path}")
        return None
    return cv2.imdecode(data, cv2.IMREAD_COLOR)

def merge_video(image_folder):

    image_folder = Path(image_folder)

    # image_folder example:
    # data/用户1-丹妮/1/1-1/1-1-1/after_preprocess_2/NYX650_...

    # Go up to segment folder (1-1-1)
    user_folder = image_folder.parent
    data_folder = user_folder.parent 
    #data_folder = action_folder.parent

    output_folder = Path('LM_video') / f"{data_folder.name}_new" / user_folder.name / image_folder.name

    output_video = "Thermal.mp4"

    os.makedirs(output_folder, exist_ok=True)


    output_path = os.path.join(output_folder, output_video)


    #print(image_folder)


    # Optional: sort image files
    images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg") and img.startswith("frame_")])
    if not images:
        print(f"No Color images found in {image_folder}")
        return
    # Read the first image to get the frame size
    first_frame = imread_unicode(str(image_folder / images[0]))
    print (first_frame)
    if first_frame is None:
        print(f"Failed to read the first image: {image_folder / images[0]}")
        return
    height, width, layers = first_frame.shape
    frame_size = (width, height)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID'
    fps = 25  # Adjust as needed
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    # Write each frame
    for image_name in images:
        img_path = os.path.join(image_folder, image_name)
        frame = imread_unicode(img_path)
        out.write(frame)

    out.release()
    print(f"Video saved to {output_video}")



def process_nyx_folder(nyx_folder: Path):
    merge_video(nyx_folder)
    #merge_IR(nyx_folder)

def walk_all_users(data_root: Path):

    #for action_folder in data_root.iterdir():  # e.g. 34坐下
    #    if not action_folder.is_dir():
    #        continue

    for user_folder in data_root.iterdir():  # e.g. user9
        if not user_folder.is_dir():
            continue

        # find sublevel folders inside user folder
        for sublevel_folder in user_folder.iterdir():  # e.g. 1-1-1
            if not sublevel_folder.is_dir():
                continue

            process_nyx_folder(sublevel_folder)

# Run it
walk_all_users(Path("LM_data/Thermal"))


def merge_color_singular():
    image_folder = r'data\用户1-丹妮\1\1-2/1-2-3/after_preprocess_2'
    image_folder = r'1-1-1\after_preprocess_2\NYX650_2025_05_07_11_48_37_0167'
    output_folder = r'video\1\1-1\1-1-1'
    output_video = 'Color_1-1-1.mp4'

    os.makedirs(output_folder, exist_ok=True)

    # Full output path including filename
    output_path = os.path.join(output_folder, output_video)

    # Optional: sort image files
    images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg") and img.startswith("Color_")])

    # Read the first image to get the frame size
    first_frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = first_frame.shape
    frame_size = (width, height)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID'
    fps = 10  # Adjust as needed
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    # Write each frame
    for image_name in images:
        img_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(img_path)
        out.write(frame)

    out.release()
    print(f"Video saved to {output_video}")
