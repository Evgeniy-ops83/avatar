from fineTuneService.ftConfiguration.ftTrainConfig import DATASET_SAVE_DIR

from datetime import datetime, date
import json
import uuid


class DatasetFile:
    id: str
    process_id: str
    filename: str
    created: str

    def __init__(self, process_id):
        self.id = str(uuid.uuid4())
        self.process_id = process_id
        self.filename = 'undefined'
        self.created = str(datetime.now())

    def saveTrainFile(self, dataset, file_name):

        self.filename = f"{file_name} - {date.today()}"
        filepath = f"{DATASET_SAVE_DIR} - {date.today()}"
        with open(filepath, 'a+') as f:
            f.write(json.dumps(dataset) + "\n")

        return filepath

