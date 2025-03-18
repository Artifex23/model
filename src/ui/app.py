import gradio as gr
import os
import json
from src.utils.image_processing import prepare_images
from src.training.trainer import StableDiffusionTrainer
from src.inference.generator import ImageGenerator

# Funktion zur Erstellung von Metadaten
def create_metadata(image_files, descriptions, output_dir):
    metadata_path = os.path.join(output_dir, "metadata.jsonl")
    with open(metadata_path, 'w') as f:
        for image_file, description in zip(image_files, descriptions):
            metadata = {
                "file_name": image_file,
                "text": description
            }
            f.write(json.dumps(metadata) + '\n')
    return metadata_path

# Gradio Interface erstellen
def create_demo():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # 🎨 Stable Diffusion Training Studio
        Trainieren Sie Ihr eigenes Stable Diffusion Modell und generieren Sie Bilder
        """)
        
        with gr.Tabs():
            # === TRAINING TAB ===
            with gr.Tab("🔧 Training"):
                with gr.Row():
                    with gr.Column():
                        # Modell-Konfiguration
                        with gr.Group():
                            gr.Markdown("### Modell-Konfiguration")
                            base_model = gr.Dropdown(
                                choices=[
                                    "stabilityai/stable-diffusion-2-1",
                                    "CompVis/stable-diffusion-v1-4",
                                    "runwayml/stable-diffusion-v1-5"
                                ],
                                label="Basis Modell",
                                value="stabilityai/stable-diffusion-2-1"
                            )
                        
                        # Bildupload
                        images = gr.File(
                            label="Trainingsbilder hochladen",
                            file_count="multiple",
                            file_types=["image"]
                        )
                        
                        descriptions = gr.Textbox(
                            label="Bildbeschreibungen (eine pro Zeile)",
                            lines=5,
                            placeholder="Geben Sie für jedes Bild eine Beschreibung ein..."
                        )
                        
                        model_name = gr.Textbox(
                            label="Modellname",
                            placeholder="Geben Sie den gewünschten Modellnamen ein..."
                        )
                        
                        learning_rate = gr.Number(
                            label="Lernrate",
                            value=1e-5,
                            precision=6
                        )
                        
                        epochs = gr.Number(
                            label="Epochen",
                            value=10,
                            precision=0
                        )
                        
                        train_btn = gr.Button("🚀 Training starten")
                        status_output = gr.Textbox(label="Status", interactive=False)
                
                # Event Handler für das Training
                def start_training(base_model, images, descriptions, model_name, learning_rate, epochs):
                    # Bilder vorbereiten
                    input_directory = "data/raw"
                    output_directory = "data/processed"
                    prepare_images(input_directory, output_directory)
                    
                    # Metadaten erstellen
                    image_files = os.listdir(output_directory)
                    metadata_path = create_metadata(image_files, descriptions.split('\n'), output_directory)
                    
                    # Training starten
                    trainer = StableDiffusionTrainer(base_model, learning_rate, epochs, model_name)
                    trainer.train(output_directory, metadata_path)
                    return "Training abgeschlossen!"
                
                train_btn.click(
                    fn=start_training,
                    inputs=[base_model, images, descriptions, model_name, learning_rate, epochs],
                    outputs=[status_output]
                )
                
            # === GENERATION TAB ===
            with gr.Tab("🎨 Bildgenerierung"):
                with gr.Row():
                    with gr.Column():
                        prompt = gr.Textbox(
                            label="Prompt",
                            placeholder="Beschreiben Sie das gewünschte Bild..."
                        )
                        negative_prompt = gr.Textbox(
                            label="Negative Prompt",
                            placeholder="Was soll nicht im Bild erscheinen..."
                        )
                        num_steps = gr.Slider(
                            minimum=1,
                            maximum=100,
                            value=50,
                            step=1,
                            label="Anzahl der Schritte"
                        )
                        guidance_scale = gr.Slider(
                            minimum=1,
                            maximum=20,
                            value=7.5,
                            step=0.1,
                            label="Guidance Scale"
                        )
                        width = gr.Slider(
                            minimum=256,
                            maximum=1024,
                            value=512,
                            step=64,
                            label="Bildbreite"
                        )
                        height = gr.Slider(
                            minimum=256,
                            maximum=1024,
                            value=512,
                            step=64
                        )
                        seed = gr.Number(
                            label="Seed (-1 für zufällig)",
                            value=-1,
                            step=1
                        )
                        generate_btn = gr.Button("Bild generieren")
                    with gr.Column():
                        output_image = gr.Image(label="Generiertes Bild")
        
        return demo

# Exportieren Sie die Funktion, um die Gradio-App zu erstellen 