import os

def create_project_structure():
    # Hauptverzeichnisse
    directories = {
        "models": {  # Für trainierte Modelle
            "checkpoints": {},
            "final": {}
        },
        "data": {  # Für Trainingsdaten
            "raw": {},
            "processed": {},
            "metadata": {}
        },
        "outputs": {  # Für generierte Bilder und Logs
            "generated_images": {},
            "logs": {},
            "training_results": {}
        },
        "configs": {},  # Für Konfigurationsdateien
        "cache": {}    # Für temporäre Dateien
    }
    
    # Erstelle die Verzeichnisstruktur
    for main_dir, subdirs in directories.items():
        for subdir, _ in subdirs.items():
            path = os.path.join(main_dir, subdir)
            os.makedirs(path, exist_ok=True)
        if not subdirs:  # Wenn keine Unterverzeichnisse
            os.makedirs(main_dir, exist_ok=True)
    
    print("✅ Projektstruktur wurde erstellt:")
    print("""
    project/
    ├── models/
    │   ├── checkpoints/    # Für Zwischenspeicherungen während des Trainings
    │   └── final/         # Für fertig trainierte Modelle
    ├── data/
    │   ├── raw/           # Originale Trainingsbilder
    │   ├── processed/     # Vorverarbeitete Trainingsdaten
    │   └── metadata/      # Bildbeschreibungen und Metadaten
    ├── outputs/
    │   ├── generated_images/  # Generierte Bilder
    │   ├── logs/             # Trainingslogs
    │   └── training_results/ # Trainingsmetriken und Visualisierungen
    ├── configs/           # Konfigurationsdateien
    └── cache/            # Temporäre Dateien
    """)

    # Erstelle .gitignore
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
    
    print("✅ .gitignore wurde erstellt") 