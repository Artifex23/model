import os
from src.utils.project_structure import create_project_structure
from src.ui.app import create_demo
from src.utils.model_utils import download_model

def main():
    # Erstelle Projektstruktur
    create_project_structure()
    
    # Basis-Modell herunterladen
    base_model_name = "stabilityai/stable-diffusion-2-1"
    download_model(base_model_name)
    
    # Erstelle und starte die Gradio App
    demo = create_demo()
    demo.launch(server_name="127.0.0.1", server_port=7860)

if __name__ == "__main__":
    main() 