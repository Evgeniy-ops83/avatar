from ftModels.Dataset import Dataset
from openaiConnector.completion import ChatCompletion
from ftConfiguration.ftTrainConfig import COMPANY_URL
from ftFileManage.saveTrainDataset import DatasetFile
from ftStorage.ftPgConnector import saveObjectDataset

import uuid
from datetime import datetime


class FtProcess:  # for api return process
    id: str
    company_name: str
    created: str
    path: str

    def __init__(self, company_name):
        self.id = str(uuid.uuid4())
        self.company_name = company_name
        self.created = str(datetime.now())
        self.path = 'undefined'

    def createRequestFromTemplate(self, question):  # Create newDataset from template

        print(f'The next question is {question}')

        SysDataset = Dataset(
            process_id=self.id,
            ds_type='system_request'
        )
        SystemObject = (SysDataset
                        .createDataset(company_name=self.company_name))

        UsrDataset = Dataset(
            process_id=self.id,
            ds_type='user_request'
        )
        UserObject = (UsrDataset
                      .createDataset(company_name=self.company_name, question=question))

        completion_dataset = [SystemObject, UserObject]

        saveObjectDataset(object=SysDataset.__dict__)
        saveObjectDataset(object=UsrDataset.__dict__)

        print('completion_dataset - ', completion_dataset)
        '''
        >>>
        [
        {"role": "system","content": "Write the answer to the question in the format ... into the value"}, 
        {"role": "user", "content": "Write an answer to the question about the comp...delivery of company products?"}
        ]
        '''

        return completion_dataset

    def getTrainCompletion(self, request_completion):  # Send request to ChatGPT

        train_completion = (ChatCompletion(
            request_completion
        ).getCompletionJson())
        print('train_completion - ', train_completion)

        '''
        train_completion
        {
        'user_request': 'How can I get delivery of company products?', 
        'assistant_request': 'You can get delivery of company products by pla...erred shipping method during checkout.'
        }
        '''

        return train_completion

    def createTrainDataset(self, request):  # Format GPT response for Train Dataset

        UsrDataset = Dataset(
            process_id=self.id,
            ds_type='user_completion'
        )
        UsrObject = (UsrDataset
                     .createDataset(company_name=self.company_name, **request))

        AssistDataset = Dataset(
            process_id=self.id,
            ds_type='assist_completion'
        )
        AssistObject = (AssistDataset
                        .createDataset(company_name=self.company_name, **request))

        train_dataset = {'messages': [UsrObject, AssistObject]}

        saveObjectDataset(object=UsrDataset.__dict__)
        saveObjectDataset(object=AssistDataset.__dict__)

        print('train_dataset - ', train_dataset)

        '''
        train_dataset  
        {'messages': 
            [
            {'role': 'user', 'content': 'What is the key feedback points about the company from customers?'}, 
            {'role': 'assistant', 'content': 'Customers praise Eleven Labs for its powerful AI capa...ndly interface.'}
            ]
        }
        '''
        
        return train_dataset

    def saveDatasetFile(self, dataset):

        dataset_file = DatasetFile(self.id)
        self.path = dataset_file.saveTrainFile(dataset, self.company_name)  # Save Train Dataset
        print('dataset_path - ', self.path)

        return self.path
        



