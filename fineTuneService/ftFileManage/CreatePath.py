from ftConfiguration.ftTrainConfig import FINE_TUNE_DATASET_DIR, FINE_TUNE_DATASET
from pathlib import Path
from datetime import datetime


def createDir(dataset_name):
    data_folder = Path(FINE_TUNE_DATASET_DIR)
    print(data_folder)
    file_to_open = data_folder / FINE_TUNE_DATASET
    print(file_to_open)
    f = open(file_to_open)
    print(f.read())

