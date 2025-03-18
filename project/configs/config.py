# Konfigurationsdatei für das Projekt
config = {
    "pretrained_model_name": "stabilityai/stable-diffusion-2-1",
    "learning_rate": 1e-5,
    "max_train_steps": 1000,
    "train_batch_size": 4,
    "gradient_accumulation_steps": 4,
    "mixed_precision": "fp16",
    "seed": 42
} 