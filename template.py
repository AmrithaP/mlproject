import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_files =[
  #".github/workflows/.gitkeep", # github folder
  f"src/{project_name}/__init__.py",
  f"src/{project_name}/components/__init__.py",
  f"src/{project_name}/components/data_ingestion.py",
  f"src/{project_name}/components/data_transformation.py",
  f"src/{project_name}/components/model_trainer.py",
  f"src/{project_name}/components/model_monitoring.py",
  f"src/{project_name}/pipelines/__init__.py",
  f"src/{project_name}/pipelines/training_pipeline.py",
  f"src/{project_name}/pipelines/prediction_pipeline.py",
  f"src/{project_name}/exception.py",
  f"src/{project_name}/logger.py",
  f"src/{project_name}/utils.py",
  "app.py",
  "Dockerfile",
  "requirements.txt",
  "setup.py",
  "main.py"
]


for file_path in list_of_files:
    filepath = Path(file_path)
    filedir = filepath.parent  # Get the parent directory

    # Check if the directory is not empty before creating it
    if filedir != Path('.'):  # Ensures it is not the current directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating file directory: {filedir}")

    # Create the file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating an empty File: {filepath}")
    else:
        logging.info(f"{filepath.name} already exists")