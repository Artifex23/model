from PIL import Image
import os

def prepare_images(input_dir, output_dir, target_size=(512, 512)):
    """
    Bereitet Bilder für das Training vor
    """
    os.makedirs(output_dir, exist_ok=True)
    
    processed_images = []
    for image_file in os.listdir(input_dir):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_dir, image_file)
            
            # Bild laden und konvertieren
            with Image.open(image_path) as img:
                # Zu RGB konvertieren (falls PNG mit Transparenz)
                img = img.convert('RGB')
                
                # Auf richtige Größe bringen
                img = img.resize(target_size, Image.Resampling.LANCZOS)
                
                # Speichern
                output_path = os.path.join(output_dir, image_file)
                img.save(output_path, quality=95)
                processed_images.append(output_path)
    
    return processed_images 