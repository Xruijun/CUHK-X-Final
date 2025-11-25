from mmpose.apis import MMPoseInferencer
import os
from glob import glob
# 使用 3D 模型别名构建推理器
inferencer = MMPoseInferencer(pose3d="human3d")

# 使用 3D 模型配置名构建推理器
inferencer = MMPoseInferencer(pose3d="motionbert_dstformer-ft-243frm_8xb32-120e_h36m")

# 使用 3D 模型配置文件和权重文件的路径或 URL 构建推理器
inferencer = MMPoseInferencer(
    pose3d='configs/body_3d_keypoint/motionbert/h36m/' \
           'motionbert_dstformer-ft-243frm_8xb32-120e_h36m.py',
    pose3d_weights='https://download.openmmlab.com/mmpose/v1/body_3d_keypoint/' \
                   'pose_lift/h36m/motionbert_ft_h36m-d80af323_20230531.pth'
)

OG_dir = '/aiot-nvme-15T-x2-hk01/siyang/CUHK-X/LM_data/'

root_dir = os.path.join(OG_dir, 'RGB')
for user_name in os.listdir(root_dir):
       user_path = os.path.join(root_dir, user_name)
       for label_name in os.listdir(user_path):
              print(f"Processing user: {user_name}, label: {label_name}")
              label_path = os.path.join(user_path, label_name)
              img_files = sorted(glob(os.path.join(label_path, 'Color*.jpg')))
              save_dir = os.path.join(OG_dir, 'Skeleton')
              os.makedirs(save_dir, exist_ok=True)

              for img_path in img_files:
                     temp_dir = os.path.join(save_dir, user_name)
                     vis_dir = os.path.join(temp_dir, label_name)
                     os.makedirs(vis_dir, exist_ok=True)
                     if os.path.basename(img_path) in os.listdir(vis_dir):
                            print(f"Skipping {img_path} as it already exists in {save_dir}")
                            continue
                     result_generator = inferencer(img_path, out_dir=save_dir)
                     result = next(result_generator)

