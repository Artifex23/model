from diffusers import StableDiffusionPipeline
import os
import torch

def download_model(model_name, model_dir="models/checkpoints"):
    os.makedirs(model_dir, exist_ok=True)
    
    model_path = os.path.join(model_dir, model_name.replace('/', '_'))
    if not os.path.exists(model_path):
        print(f"Modell {model_name} wird heruntergeladen...")
        try:
            pipeline = StableDiffusionPipeline.from_pretrained(
                model_name,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                low_cpu_mem_usage=True,
                device_map="auto",
                offload_folder="offload"
            )
            pipeline.save_pretrained(model_path)
            print(f"Modell {model_name} wurde heruntergeladen und gespeichert unter {model_path}.")
        except Exception as e:
            print(f"Fehler beim Herunterladen des Modells: {e}")
    else:
        print(f"Modell {model_name} ist bereits vorhanden unter {model_path}.")
    return model_path 