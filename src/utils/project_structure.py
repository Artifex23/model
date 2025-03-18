import os

def create_project_structure():
    directories = {
        "models": {
            "checkpoints": {},
            "final": {}
        },
        "data": {
            "raw": {},
            "processed": {},
            "metadata": {}
        },
        "outputs": {
            "generated_images": {},
            "logs": {},
            "training_results": {}
        },
        "configs": {},
        "cache": {}
    }
    
    for main_dir, subdirs in directories.items():
        for subdir, _ in subdirs.items():
            path = os.path.join(main_dir, subdir)
            os.makedirs(path, exist_ok=True)
        if not subdirs:
            os.makedirs(main_dir, exist_ok=True)
    
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Projektspezifisch
cache/
outputs/generated_images/
outputs/logs/
models/checkpoints/
*.ckpt
*.safetensors

# IDEs
.idea/
.vscode/
*.swp
*.swo
    """
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content.strip()) 