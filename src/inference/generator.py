import torch
from diffusers import StableDiffusionPipeline
from transformers import CLIPTokenizer

class ImageGenerator:
    def __init__(self, model_path, tokenizer_path):
        self.pipeline = StableDiffusionPipeline.from_pretrained(
            model_path,
            torch_dtype=torch.float16
        ).to("cuda")
        self.tokenizer = CLIPTokenizer.from_pretrained(tokenizer_path)

    def generate_image(self, prompt, negative_prompt="", num_steps=50, guidance_scale=7.5, width=512, height=512, seed=None):
        # Tokenisierung des Prompts
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        
        # Seed setzen
        generator = torch.Generator("cuda").manual_seed(seed) if seed is not None else None
        
        # Bild generieren
        with torch.cuda.amp.autocast():
            image = self.pipeline(
                prompt=inputs.input_ids,
                negative_prompt=negative_prompt,
                num_inference_steps=num_steps,
                guidance_scale=guidance_scale,
                width=width,
                height=height,
                generator=generator
            ).images[0]
        
        return image 