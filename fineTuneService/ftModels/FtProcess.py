from ftModels.Dataset import Dataset, DatasetBuilder
from openai.completion import ChatCompletion
from ftConfiguration.ftTrainConfig import COMPANY_URL
from ftFileManage.saveTrainDataset import DatasetFile
from ftStorage.ftClickhouseConnector import saveSourceObject

import uuid
from datetime import datetime


class FtProcess:  # for api return process
    id: str
    company_url: str
    created: str

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.company_url = COMPANY_URL
        self.created = str(datetime.now())

    def createRequestFromTemplate(self, question):  # Create request from template

        print(f'The next question is {question}')

        request_template = DatasetBuilder()
        system_template = request_template.createDatasetFromTemplate(question, 'system_request')
        user_template = request_template.createDatasetFromTemplate(question, 'user_request')

        system_dataset_obj = Dataset('system_request', self.id)
        system_dataset = system_dataset_obj.createDataset(system_template)

        user_dataset_obj = Dataset('user_request', self.id)
        user_dataset = user_dataset_obj.createDataset(user_template)

        saveSourceObject('dataset', system_dataset_obj.__dict__)
        saveSourceObject('dataset', user_dataset_obj.__dict__)

        request_completion = request_template.createDatasetList(system_dataset, user_dataset)
        print('request_completion - ', request_completion)

        return request_completion

    def getTrainCompletion(self, request_completion):  # Send request to ChatGPT

        train_completion = ChatCompletion(request_completion).getCompletionJson()
        print('train_completion - ', train_completion)

        return train_completion

    def createTrainDataset(self, request):  # Format GPT response for Train Dataset

        train_template = DatasetBuilder()
        user_train_completion = train_template.createTrainDataset('user_completion', request['user_request'])
        assist_train_completion = train_template.createTrainDataset('assist_completion', request['assistant_request'])

        user_completion_obj = Dataset('user_completion', self.id)
        user_completion_ds = user_completion_obj.createDataset(user_train_completion)

        assist_completion_obj = Dataset('assist_completion', self.id)
        assist_completion_ds = assist_completion_obj.createDataset(assist_train_completion)

        saveSourceObject('dataset', user_completion_obj.__dict__)
        saveSourceObject('dataset', assist_completion_obj.__dict__)

        train_completion_list = train_template.createDatasetList(user_completion_ds, assist_completion_ds)
        train_dataset = train_template.createMessageTrainList(train_completion_list)
        print('train_dataset - ', train_dataset)

        return train_dataset

    def saveDatasetFile(self, dataset):

        dataset_file = DatasetFile(self.id)
        dataset_path = dataset_file.saveTrainFile(dataset, self.company_url)  # Save Train Dataset
        print('dataset_path - ', dataset_path)

        saveSourceObject('ds_file', dataset_file.__dict__)

        return dataset_path
