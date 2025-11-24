import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
import numpy as np
import os
from io import BytesIO, StringIO
from PIL import Image

# --- ???? ---
CSV_PATH = "radar.csv"  # ?? CSV ????
OUTPUT_VIDEO = "3d_coordinates_video.mp4"  # ??????
FPS = 10  # ????
VIDEO_SIZE = (1280, 720)  # ????? (?, ?)
DPI = 150  # ????? DPI
POINT_SIZE = 100  # 3D ????

# --- ???????? ---
def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)
    unique_timestamps = df["timestamp"].unique()
    return df, unique_timestamps

# --- ????? ---
def create_3d_frame(df, timestamp, unique_objects):
    current_data = df[df["timestamp"] == timestamp].reset_index(drop=True)
    
    # ????
    fig = plt.figure(figsize=(VIDEO_SIZE[0]/DPI, VIDEO_SIZE[1]/DPI), dpi=DPI)
    ax = fig.add_subplot(111, projection='3d')
    
    # ?????????????????
    ax.set_xlim([-3, 3])  # ??????????
    ax.set_ylim([-3, 5])  # ??????????
    ax.set_zlim([-3, 3])  # ??????????
    
    ax.set_xlabel('X (m)', fontsize=12)
    ax.set_ylabel('Y (m)', fontsize=12)
    ax.set_zlabel('Z (m)', fontsize=12)
    ax.set_title(f'3D Object Trajectories\nTimestamp: {timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}', fontsize=14, pad=20)
    
    # ?????????
    colors = plt.cm.get_cmap("hsv", len(unique_objects))
    obj_color_map = {obj: colors(i) for i, obj in enumerate(unique_objects)}
    
    # ??????????
    for _, row in current_data.iterrows():
        det_obj = int(row["DetObj#"])
        x, y, z = row["x"], row["y"], row["z"]
        ax.scatter(x, y, z, c=[obj_color_map[det_obj]], s=POINT_SIZE, label=f'Obj {det_obj}' if det_obj in unique_objects[:10] else "") # ????10???

    # ????
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1), fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # ????
    ax.view_init(elev=20, azim=45)
    
    # ?matplotlib?????OpenCV??
    buf = BytesIO()
    plt.tight_layout()
    fig.savefig(buf, format='png', dpi=DPI, bbox_inches='tight')
    buf.seek(0)
    img = Image.open(buf)
    img_array = np.array(img)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    plt.close(fig)
    return img_array

# --- ??????? ---
def generate_3d_video():
    df, unique_timestamps = load_and_preprocess_data(CSV_PATH)
    
    # ??????????ID
    unique_objects = sorted(df["DetObj#"].unique())
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, FPS, VIDEO_SIZE)
    
    total_frames = len(unique_timestamps)
    print(f"???????? {total_frames} ???? {FPS} FPS...")
    
    for i, timestamp in enumerate(unique_timestamps):
        frame = create_3d_frame(df, timestamp, unique_objects)
        frame = cv2.resize(frame, VIDEO_SIZE)
        out.write(frame)
        
        if (i + 1) % max(1, total_frames // 10) == 0:
            print(f"??? {i + 1}/{total_frames} ? ({((i + 1)/total_frames)*100:.1f}%)")

    out.release()
    cv2.destroyAllWindows()
    print(f"????????????{os.path.abspath(OUTPUT_VIDEO)}")

# --- ?? ---
if __name__ == "__main__":
    if not os.path.exists(CSV_PATH):
        print(f"{CSV_PATH}")
    else:
        generate_3d_video()