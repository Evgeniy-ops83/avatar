from fineTuneService.ftModels.dataset import Dataset, DatasetBuilder
from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftConfiguration.ftTrainConfig import COMPANY_URL, QUESTION_LIST
from fineTuneService.ftFileManage.saveTrainDataset import saveTrainFile

import uuid
from datetime import datetime


class FtProcess:
    ID: str
    COMPANY_URL: str
    CREATED: str
    QUESTION_SET: str

    def __init__(self):
        self.ID = str(uuid.uuid4())
        self.COMPANY_URL = COMPANY_URL
        self.CREATED = str(datetime.now())
        self.QUESTION_SET = QUESTION_LIST

    def createRequestFromTemplate(self, question):  # Create request from template

        print(f'The next question is {question}')

        request_template = DatasetBuilder()
        system_template = request_template.createDatasetFromTemplate(question, 'system_request')
        user_template = request_template.createDatasetFromTemplate(question, 'user_request')

        system_dataset = Dataset('system_request', self.ID).createDataset(system_template)
        user_dataset = Dataset('user_request', self.ID).createDataset(user_template)

        request_completion = request_template.createDatasetList(system_dataset, user_dataset)
        print('request_completion - ', request_completion)

        return request_completion

    def getTrainCompletion(self, request_completion):  # Send request to ChatGPT

        # {'user_request': 'List 3 last events in which Snickers participated lately?', 'assistant_request': 'null'}

        train_completion = ChatCompletion(request_completion).getCompletionJson()
        print('train_completion - ', train_completion)

        return train_completion

    def createTrainDataset(self, request):  # Format GPT response for Train Dataset

        train_template = DatasetBuilder()
        user_train_completion = train_template.createTrainDataset('user_completion', request['user_request'])
        assist_train_completion = train_template.createTrainDataset('assist_completion', request['assistant_request'])

        user_completion_ds = Dataset('user_completion', self.ID).createDataset(user_train_completion)
        assist_completion_ds = Dataset('assist_completion', self.ID).createDataset(assist_train_completion)

        train_completion_list = train_template.createDatasetList(user_completion_ds, assist_completion_ds)
        train_dataset = train_template.createMessageTrainList(train_completion_list)
        print('train_dataset - ', train_dataset)

        return train_dataset

    def saveDatasetFile(self, dataset):

        dataset_path = saveTrainFile(dataset)  # Save Train Dataset
        print('dataset_path - ', dataset_path)

        return dataset_path

'''
a = createNewTrainDataset()
print(a)
'''