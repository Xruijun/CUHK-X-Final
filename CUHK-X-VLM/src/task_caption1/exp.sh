CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_caption1/main_videochatr1_choices.py --modality ir
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_caption1/main_videochatr1_choices.py --modality depth

CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_caption2/main_videochatr1_choices.py --modality ir
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_caption2/main_videochatr1_choices.py --modality depth
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_caption2/main_videochatr1_choices.py --modality thermal

# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption1/main_internvl_choices.py --modality ir --model_size 8B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_internvl_choices.py --modality ir --model_size 8B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_internvl_choices.py --modality rgb --model_size 8B

# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_internvl_choices.py --modality ir --model_size 2B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_qwenvl_choices.py --modality ir --model_size 3B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_qwenvl_choices.py --modality ir --model_size 7B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption1/main_videochatr1_choices.py --modality ir
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_videochatr1_choices.py --modality ir

# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_internvl_choices.py --modality depth --model_size 2B
CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_internvl_choices.py --modality depth --model_size 8B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_qwenvl_choices.py --modality depth --model_size 3B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_qwenvl_choices.py --modality depth --model_size 7B
CUDA_VISIBLE_DEVICES=3,5 python src/task_caption1/main_videochatr1_choices.py --modality depth

# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_internvl_choices.py --modality thermal --model_size 2B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_internvl_choices.py --modality thermal --model_size 8B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_qwenvl_choices.py --modality thermal --model_size 3B
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_qwenvl_choices.py --modality thermal --model_size 7B
CUDA_VISIBLE_DEVICES=3,5 python src/task_caption1/main_videochatr1_choices.py --modality thermal



# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption1/main_videollava_choices.py --modality thermal
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption1/main_videollava_choices.py --modality depth
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption1/main_videollava_choices.py --modality rgb
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption1/main_videollava_choices.py --modality ir

# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_videollava_choices.py --modality thermal
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_videollava_choices.py --modality depth
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_videollava_choices.py --modality rgb
# CUDA_VISIBLE_DEVICES=3,5 python src/task_caption2/main_videollava_choices.py --modality ir

# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_internvl_choices.py --modality ir --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_internvl_choices.py --modality ir --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_qwenvl_choices.py --modality ir --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_qwenvl_choices.py --modality ir --model_size 7B

# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_internvl_choices.py --modality ir --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_internvl_choices.py --modality ir --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_qwenvl_choices.py --modality ir --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_qwenvl_choices.py --modality ir --model_size 7B

# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_internvl_choices.py --modality depth --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_internvl_choices.py --modality depth --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_qwenvl_choices.py --modality depth --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_qwenvl_choices.py --modality depth --model_size 7B

# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_internvl_choices.py --modality depth --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_internvl_choices.py --modality depth --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_qwenvl_choices.py --modality depth --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_qwenvl_choices.py --modality depth --model_size 7B

# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_internvl_choices.py --modality thermal --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_internvl_choices.py --modality thermal --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_qwenvl_choices.py --modality thermal --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption2/main_qwenvl_choices.py --modality thermal --model_size 7B

# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_internvl_choices.py --modality thermal --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_internvl_choices.py --modality thermal --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_qwenvl_choices.py --modality thermal --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,5,6,7 python src/task_caption1/main_qwenvl_choices.py --modality thermal --model_size 7B

# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption2/main_internvl_choices.py --modality rgb --model_size 2B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption2/main_internvl_choices.py --modality rgb --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption2/main_qwenvl_choices.py --modality rgb --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption2/main_qwenvl_choices.py --modality rgb --model_size 7B

# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption1/main_internvl_choices.py --modality rgb --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption1/main_internvl_choices.py --modality rgb --model_size 8B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption1/main_qwenvl_choices.py --modality rgb --model_size 3B
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption1/main_qwenvl_choices.py --modality rgb --model_size 7B


# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption2/main_videochatr1_choices.py
# CUDA_VISIBLE_DEVICES=0,1,3,6,7 python src/task_caption1/main_videochatr1_choices.py --modality rgb
