from fineTuneService.ftConfiguration.ftTrainConfig import DATASET_SAVE_DIR

from datetime import datetime, date
import json


def saveTrainFile(dataset):

    filepath = f"{DATASET_SAVE_DIR} - {date.today()}"
    with open(filepath, 'a+') as f:
        f.write(json.dumps(dataset) + "\n")

    return filepath

