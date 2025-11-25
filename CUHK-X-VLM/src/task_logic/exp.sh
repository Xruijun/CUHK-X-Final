# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_internvl_choices.py --modality rgb --model_size 2B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_internvl_choices.py --modality rgb --model_size 8B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_videollava_choices.py --modality rgb

# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_internvl_choices.py --modality ir --model_size 2B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_internvl_choices.py --modality ir --model_size 8B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality ir --model_size 3B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality ir --model_size 7B

CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality rgb --model_size 3B
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality rgb --model_size 7B
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality depth --model_size 3B
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality depth --model_size 7B
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_videochatr1_choices.py --modality rgb
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_videochatr1_choices.py --modality depth

# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_videollava_choices.py --modality ir

# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_internvl_choices.py --modality depth --model_size 2B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_internvl_choices.py --modality depth --model_size 8B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_videollava_choices.py --modality depth

# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_videochatr1_choices.py --modality ir