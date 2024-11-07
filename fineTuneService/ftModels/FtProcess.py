from ftModels.Dataset import Dataset, DatasetBuilder
from openaiConnector.completion import ChatCompletion
from ftConfiguration.ftTrainConfig import COMPANY_URL
from ftFileManage.saveTrainDataset import DatasetFile
from ftStorage.ftPgConnector import saveObject

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

        SystemRequest = (Object
                         .createDatasetFromTemplate(question, ds_type='system_request'))
        SystemObject = (Object
                        .createNewDataset(ds_type='system_request', request=SystemRequest))

        UserRequest = (Object
                       .createCustomDataset(question, self.company_name, ds_type='user_request'))
        UserObject = (Object
                      .createNewDataset(ds_type='user_request', request=SystemRequest))

        saveObject(table='dataset', object=SystemObject.__dict__)
        saveObject(table='dataset', object=UserObject.__dict__)

        completion_dataset = Object.createDatasetList(
            SystemRequest,
            UserRequest
        )

        print('completion_dataset - ', completion_dataset)

        return completion_dataset

    def getTrainCompletion(self, request_completion):  # Send request to ChatGPT

        train_completion = (ChatCompletion(
            request_completion
        ).getCompletionJson())
        print('train_completion - ', train_completion)

        return train_completion

    '''
    def createTrainDataset(self, request):  # Format GPT response for Train Dataset

        ds_type = 'user_completion'
        process_id = self.id

        userCompletion = DatasetBuilder(
            ds_type,
            process_id
        ).createTrainDataset(
            ds_type,
            request=request['user_request']
        )

        ds_type = 'assist_completion'
        process_id = self.id

        assistCompletion = DatasetBuilder(
            ds_type,
            process_id
        ).createTrainDataset(
            ds_type,
            request=request['assistant_request']
        )

        saveObject('dataset', userCompletion.__dict__)
        saveObject('dataset', assistCompletion.__dict__)

        
        train_completion_list = (train_template
                                 .createDatasetList(user_completion_ds, assist_completion_ds))
        train_dataset = (train_template
                         .createMessageTrainList(train_completion_list))
        print('train_dataset - ', train_dataset)
        
        
        return 200

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

