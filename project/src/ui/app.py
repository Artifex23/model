import gradio as gr
import sys
import os

# Füge den Projektroot zum Python-Pfad hinzu
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from src.inference.generator import ImageGenerator
from src.training.trainer import StableDiffusionTrainer
from src.utils.project_structure import create_project_structure
from configs.config import config

# ... (Rest des Gradio UI Codes) ... 