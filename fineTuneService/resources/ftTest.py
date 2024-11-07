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


