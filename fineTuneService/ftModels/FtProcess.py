from ftModels.Dataset import Dataset, DatasetBuilder
from openaiConnector.completion import ChatCompletion
from ftConfiguration.ftTrainConfig import COMPANY_URL
from ftFileManage.saveTrainDataset import DatasetFile


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

    def createRequestFromTemplate(self, question):  # Create newDataset from template

        print(f'The next question is {question}')

        Object = DatasetBuilder(
            process_id=self.id
        )

        SystemTemplate = (Object
                          .createDatasetFromTemplate(question, ds_type='system_request'))
        UserTemplate = (Object
                        .createCustomDataset(question, self.company_name, ds_type='user_request'))

        SystemObject = (Object
                        .createNewDataset(ds_type='system_request', request=SystemTemplate))
        UserObject = (Object
                      .createNewDataset(ds_type='user_request', request=UserTemplate))

        completion_dataset = Object.createDatasetList(
            SystemObject,
            UserObject
        )

        print('completion_dataset - ', completion_dataset)

        return completion_dataset

    def getTrainCompletion(self, request_completion):  # Send request to ChatGPT

        train_completion = (ChatCompletion(
            request_completion
        ).getCompletionJson())
        print('train_completion - ', train_completion)

        return train_completion


    def createTrainDataset(self, request):  # Format GPT response for Train Dataset

        Object = DatasetBuilder(
            process_id=self.id
        )

        UserObject = (Object
                      .createNewDataset(ds_type='user_completion', request=request['user_request']))
        AssistObject = (Object
                        .createNewDataset(ds_type='assist_completion', request=request['assistant_request']))

        completion_dataset = Object.createDatasetList(
            UserObject,
            AssistObject
        )

        train_dataset = (Object
                         .createMessageTrainList(completion_dataset))

        print('train_dataset - ', train_dataset)
        
        return train_dataset

    '''
    def saveDatasetFile(self, dataset, company_name):

        dataset_file = DatasetFile(self.id)
        self.path = dataset_file.saveTrainFile(dataset, self.company_name)  # Save Train Dataset
        print('dataset_path - ', self.path)

        saveDataset('ds_file', dataset_file.__dict__)

        return self.path
        
        
        
    train_completion = newProcess
    .getTrainCompletion
    (
    completion_dataset
    )

    train_dataset = (newProcess
    .createTrainDataset(train_completion))

    dataset_path = (newProcess
    .saveDatasetFile(train_dataset, company_name))

        saveObject('process', newProcess.__dict__)
            

return newProcess.__dict__
        
        '''

