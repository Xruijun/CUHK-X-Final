CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_internvl.py --modality depth --model_size 2B
CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_internvl.py --modality depth --model_size 8B
CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_qwenvl.py --modality depth --model_size 7B
CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_qwenvl.py --modality depth --model_size 3B
CUDA_VISIBLE_DEVICES=0,1,2,4,5 python src/task_caption/main_videochatr1.py --modality depth
CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_videollava.py --modality depth

# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_internvl.py --modality rgb --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_internvl.py --modality rgb --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_qwenvl.py --modality rgb --model_size 7B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_qwenvl.py --modality rgb --model_size 3B

# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_internvl.py --modality ir --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_internvl.py --modality ir --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_qwenvl.py --modality ir --model_size 7B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_qwenvl.py --modality ir --model_size 3B

# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_videollava.py --modality rgb
# CUDA_VISIBLE_DEVICES=0,1,2,4,5 python src/task_caption/main_videochatr1.py --modality rgb

# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption/main_videollava.py --modality ir
# CUDA_VISIBLE_DEVICES=0,1,2,4,5 python src/task_caption/main_videochatr1.py --modality ir

