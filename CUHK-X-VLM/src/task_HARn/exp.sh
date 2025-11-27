# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_internvl_context.py --modality rgb --model_size 2B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_internvl_context.py --modality rgb --model_size 8B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_videollava_context.py --modality rgb

# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_internvl_context.py --modality ir --model_size 2B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_internvl_context.py --modality ir --model_size 8B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_qwenvl_context.py --modality ir --model_size 3B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_qwenvl_context.py --modality ir --model_size 7B

CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality rgb --model_size 3B
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality rgb --model_size 7B
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality depth --model_size 3B
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_qwenvl_choices.py --modality depth --model_size 7B
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_videochatr1_choices.py --modality rgb
CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_logic/main_videochatr1_choices.py --modality depth

# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_videollava_context.py --modality ir

# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_internvl_context.py --modality depth --model_size 2B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_internvl_context.py --modality depth --model_size 8B
# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_videollava_context.py --modality depth

# CUDA_VISIBLE_DEVICES=3,4,5,7 python src/task_HARn/main_videochatr1_context.py --modality ir