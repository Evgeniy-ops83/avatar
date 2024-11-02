
from fineTuneService.ftConfiguration.ftTrainConfig import FINE_TUNE_DATASET_DIR, FINE_TUNE_DATASET

from fineTuneService.ftFacade.trainFacade import FtProcess
from fineTuneService.ftConfiguration.ftTrainConfig import QUESTION_LIST

test_process = FtProcess()
print(test_process)

for question in QUESTION_LIST:

    request_completion = test_process.createRequestFromTemplate(question)

    train_completion = test_process.getTrainCompletion(request_completion)

    train_dataset = test_process.createTrainDataset(train_completion)

    dataset_path = test_process.saveDatasetFile(train_dataset)


'''
from pathlib import Path
from datetime import datetime

data_folder = Path(FINE_TUNE_DATASET_DIR)
print(data_folder)
file_to_open = data_folder / FINE_TUNE_DATASET
print(file_to_open)
f = open(file_to_open)
print(f.read())
'''


