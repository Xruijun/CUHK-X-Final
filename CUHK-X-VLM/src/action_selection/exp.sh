#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_internvl_context.py --modality depth --model_size 3B
CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/task_caption1/main_internvl_choices --modality depth --model_size 8B
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_qwenvl_choices --modality depth --model_size 3B
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_qwenvl_choices --modality depth --model_size 7B
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_videochatr1_context.py --modality depth
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_videollava_choices --modality depth

#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_internvl_context.py --modality ir --model_size 3B
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_internvl_choices --modality ir --model_size 8B
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_qwenvl_choices --modality ir --model_size 3B
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_qwenvl_choices --modality ir --model_size 7B
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_videochatr1_context.py --modality ir
#CUDA_VISIBLE_DEVICES=0,1,2,3 python CUHK-X-VLM/src/action_selection/main_videollava_choices --modality ir
