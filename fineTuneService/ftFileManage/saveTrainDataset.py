from fineTuneService.ftConfiguration.ftTrainConfig import company_url, train_dataset_dir

from datetime import datetime, date
import json


def saveTrainFile(dataset):

    filepath = f"{train_dataset_dir} - {date.today()}"
    with open(filepath, 'a+') as f:
        f.write(json.dumps(dataset) + "\n")

    return filepath

