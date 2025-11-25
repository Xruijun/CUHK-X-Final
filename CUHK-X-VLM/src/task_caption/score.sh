# python src/task_caption/calculate_score.py --modality thermal --method qwenvl7B
# python src/task_caption/calculate_score.py --modality thermal --method qwenvl3B
# python src/task_caption/calculate_score.py --modality thermal --method internvl2B
# python src/task_caption/calculate_score.py --modality thermal --method internvl8B

# CUDA_VISIBLE_DEVICES=7 python src/task_caption/calculate_score.py --modality thermal --method qwenvl7B
# CUDA_VISIBLE_DEVICES=7 python src/task_caption/calculate_score.py --modality thermal --method qwenvl3B
# CUDA_VISIBLE_DEVICES=7 python src/task_caption/calculate_score.py --modality thermal --method internvl2B
# CUDA_VISIBLE_DEVICES=7 python src/task_caption/calculate_score.py --modality thermal --method internvl8B
CUDA_VISIBLE_DEVICES=7 python src/task_caption/calculate_score.py --modality thermal --method videochatr1
CUDA_VISIBLE_DEVICES=7 python src/task_caption/calculate_score.py --modality thermal --method videollava


# python src/task_caption/calculate_score.py --modality rgb --method qwenvl7B
# python src/task_caption/calculate_score.py --modality ir --method qwenvl7B
# python src/task_caption/calculate_score.py --modality rgb --method qwenvl3B
# python src/task_caption/calculate_score.py --modality ir --method qwenvl3B
# python src/task_caption/calculate_score.py --modality rgb --method internvl2B
# python src/task_caption/calculate_score.py --modality ir --method internvl2B
# python src/task_caption/calculate_score.py --modality rgb --method internvl8B
# python src/task_caption/calculate_score.py --modality ir --method internvl8B

# python src/task_caption/calculate_score.py --modality rgb --method videochatr1
# python src/task_caption/calculate_score.py --modality ir --method videochatr1
# python src/task_caption/calculate_score.py --modality rgb --method videollava
# python src/task_caption/calculate_score.py --modality ir --method videollava