from src.utils.project_structure import create_project_structure
from src.ui.app import demo
from src.utils.image_processing import prepare_images

def main():
    # Erstelle Projektstruktur
    create_project_structure()
    
    # Optional: Bilder vorbereiten
    # input_directory = "data/raw"
    # output_directory = "data/processed"
    # prepare_images(input_directory, output_directory)
    
    # Starte die Gradio App
    demo.launch(server_name="127.0.0.1", server_port=7860)

if __name__ == "__main__":
    main() 