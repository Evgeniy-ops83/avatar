'''
from fineTuneService.ftModels.Dataset import Dataset, DatasetBuilder

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

        print(f'object=SystemObject - ', SystemObject.__dict__)
        print(f'object=UserObject - ', UserObject.__dict__)

        #saveObject(table='dataset', object=SystemObject.__dict__)
        #saveObject(table='dataset', object=UserObject.__dict__)

        completion_dataset = Object.createDatasetList(
            SystemRequest,
            UserRequest
        )

        print('completion_dataset - ', completion_dataset)


a = FtProcess("ozon.ru").createRequestFromTemplate(question= "Назови имя компании ?")

'''

#from fineTuneService.ftStorage.ftPgConnector import saveObjectDataset

import uuid
from datetime import datetime

class Dataset2:
    id: str
    ds_type: str
    process_id: str
    updated: str
    ds_role: str
    content: str

    def __init__(self, ds_type, process_id):
        self.id = str(uuid.uuid4())
        self.ds_type = ds_type
        self.process_id = process_id
        self.updated = str(datetime.now())
        self.ds_role = 'undefined'
        self.content = 'undefined'

    def createDataset(self, request):

        if 'system_request' in request.keys():
            self.ds_role = 'system'
            self.content = request['system_request']
        elif 'user_request' in request.keys():
            self.ds_role = 'user'
            self.content = request['user_request']
        elif 'assistant_request' in request.keys():
            self.ds_role = 'assistant'
            self.content = request['assistant_request']

        dataset = {"role": self.ds_role, "content": self.content}

        return dataset

    def createAndSaveDataset(self, request):

        dataset = self.createDataset(request)

        print('dict - ', self.__dict__)
        print(dataset)

        return dataset


request = {
        'user_request': 'How can I get delivery of company products?',
        'assistant_request': 'You can get delivery of company products by pla...erred shipping method during checkout.'
        }

newDataset = Dataset2('test', 'test').createAndSaveDataset(request)
