from ftModels.Dataset import Dataset, DatasetBuilder
from openaiConnector.completion import ChatCompletion
from ftConfiguration.ftTrainConfig import COMPANY_URL
from ftFileManage.saveTrainDataset import DatasetFile
from ftStorage.ftPgConnector import saveDataset

import uuid
from datetime import datetime


class FtProcess:  # for api return process
    id: str
    company_name: str
    created: str

    def __init__(self, company_name):
        self.id = str(uuid.uuid4())
        self.company_name = company_name
        self.created = str(datetime.now())
        self.path = 'undefined'

    def createRequestFromTemplate(self, question, company_name):  # Create newDataset from template

        print(f'The next question is {question}')

        ds_type = 'system_request'
        process_id = self.id

        SystemDataset = DatasetBuilder(
                ds_type,
                process_id
            ).createDatasetFromTemplate(
            question
        )

        ds_type = 'user_request',
        process_id = self.id

        UserDataset = DatasetBuilder(
            ds_type,
            process_id
        ).createCustomDataset(
            question,
            self.company_name
        )

        saveDataset(SystemDataset.ds_type, SystemDataset.__dict__)
        saveDataset(UserDataset.ds_type, UserDataset.__dict__)

        completion_dataset = Dataset.createDatasetList(
            SystemDataset,
            UserDataset
        )

        print('completion_dataset - ', completion_dataset)

        return completion_dataset

    def getTrainCompletion(self, request_completion):  # Send request to ChatGPT

        train_completion = ChatCompletion(request_completion).getCompletionJson()
        print('train_completion - ', train_completion)

        return train_completion

    def createTrainDataset(self, request):  # Format GPT response for Train Dataset

        train_template = DatasetBuilder()
        user_train_completion = (train_template
                                 .createTrainDataset('user_completion', request['user_request']))
        assist_train_completion = (train_template
                                   .createTrainDataset('assist_completion', request['assistant_request']))

        user_completion_obj = Dataset('user_completion', self.id)
        user_completion_ds = (user_completion_obj
                              .createDataset(user_train_completion))

        assist_completion_obj = Dataset('assist_completion', self.id)
        assist_completion_ds = (assist_completion_obj
                                .createDataset(assist_train_completion))

        saveDataset('dataset', user_completion_obj.__dict__)
        saveDataset('dataset', assist_completion_obj.__dict__)

        train_completion_list = (train_template
                                 .createDatasetList(user_completion_ds, assist_completion_ds))
        train_dataset = (train_template
                         .createMessageTrainList(train_completion_list))
        print('train_dataset - ', train_dataset)

        return train_dataset

    def saveDatasetFile(self, dataset, company_name):

        dataset_file = DatasetFile(self.id)
        self.path = dataset_file.saveTrainFile(dataset, self.company_name)  # Save Train Dataset
        print('dataset_path - ', self.path)

        saveDataset('ds_file', dataset_file.__dict__)

        return self.path

