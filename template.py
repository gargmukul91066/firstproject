import os
from pathlib import Path

list_of_files=[
    ".github/workflow/.gitkeep",  # Placeholder to set up GitHub Actions (automation for CI/CD).
    "src/_init_.py",       #Marks this folder as a Python package.
    "src/components/_init_.py",   # Code for different ML pipeline components 
    "src/components/data_ingestion.py",     #get data
    "src/components/data_transformation.py",#clean/[prepare] data
    "src/components/model_trainer.py",   #train the ML model
    "src/components/model_evaluation.py",   #evaluate the model
    "src/pipeline/_init_.py",   #Code for how your ML pipeline runs:
    "src/pipeline/training_pipeline.py",     #train the model
    "src/pipeline/prediction_pipeline.py",     #make predictions
    "src/logger/logging.py", # Code to log messages (for debugging).
    "src/exception/exception",     #Handles errors that happen during execution.
    "src/utils/utils.py",    #Extra helper functions.
    "tests/unit/_init_.py",         #For writing unit tests (testing small parts).
    "tests/integration/_init_.py",    #For writing integration tests (testing combined parts).
    "init_setup.sh",  # A shell script to set up the project environment.
    "requirements.txt",  #List of Python libraries the project needs.
    "requirements_dev.txt",  #Extra libraries for developers (like testing tools).
    "setup.py",         #Used for packaging and installing the project.
    "setup.cfg",       #Used for packaging and installing the project.
    "pyproject.toml",       #Used for packaging and installing the project.
    "tox.ini",            #For testing your code in different Python environments.
    "experiment/experiments.ipynb"      # Jupyter notebook to play around with data, test code.
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True) #If there's a folder path, create it (only if it doesn't exist already).

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):      #If the file doesn’t exist or is empty, create an empty file.
        with open(filepath,"w") as f:
            pass   # create an empty file