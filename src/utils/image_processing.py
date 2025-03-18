from PIL import Image
import os

def prepare_images(input_dir, output_dir, target_size=(512, 512)):
    os.makedirs(output_dir, exist_ok=True)
    
    for image_file in os.listdir(input_dir):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_dir, image_file)
            
            with Image.open(image_path) as img:
                img = img.convert('RGB')
                img = img.resize(target_size, Image.Resampling.LANCZOS)
                output_path = os.path.join(output_dir, image_file)
                img.save(output_path, quality=95) 