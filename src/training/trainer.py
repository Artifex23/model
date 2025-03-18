import os
import torch
from safetensors.torch import save_file
from diffusers import StableDiffusionPipeline

class StableDiffusionTrainer:
    def __init__(self, base_model_name, learning_rate=1e-5, epochs=10, model_name="model"):
        self.base_model_name = base_model_name
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.model_name = model_name
        self.model = None

    def load_model(self):
        # Laden Sie das Modell
        self.model = StableDiffusionPipeline.from_pretrained(
            self.base_model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            low_cpu_mem_usage=True
        ).to("cuda")

    def train(self, data_dir, metadata_path):
        if self.model is None:
            self.load_model()
        
        print(f"Training gestartet mit Modell: {self.base_model_name}")
        print(f"Lernrate: {self.learning_rate}, Epochen: {self.epochs}")
        print(f"Verwende Daten aus: {data_dir}")
        print(f"Metadatenpfad: {metadata_path}")
        
        # Beispiel: Trainingsergebnisse speichern
        results_path = os.path.join("outputs", "training_results", "results.txt")
        with open(results_path, 'w') as f:
            f.write("Training abgeschlossen!\n")
        print("Training abgeschlossen!")
        
        # Modell-Checkpointing
        checkpoint_path = os.path.join("models", "checkpoints", f"{self.model_name}.safetensors")
        save_file(self.model.state_dict(), checkpoint_path)
        print(f"Modell-Checkpoint gespeichert unter: {checkpoint_path}") 