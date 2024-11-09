from ftConfiguration.ftTrainConfig import TRAIN_SYSTEM_REQUEST, TRAIN_USER_REQUEST


from pydantic import BaseModel
import uuid
from datetime import datetime


class Dataset:
    id: str
    ds_type: str
    process_id: str
    updated: str
    ds_role: str
    content: str

    def __init__(self, process_id, ds_type):
        self.id = str(uuid.uuid4())
        self.ds_type = ds_type
        self.process_id = process_id
        self.updated = str(datetime.now())
        self.ds_role = 'undefined'
        self.content = 'undefined'

    def createDataset(self, company_name, request, question=''):

        if self.ds_type == 'system_request':
            self.ds_role = 'system'
            self.content = TRAIN_SYSTEM_REQUEST

        if self.ds_type == 'user_request':
            self.ds_role = 'user'
            self.content = TRAIN_USER_REQUEST.format(company_name) + question

        if self.ds_type == 'user_completion':
            self.ds_role = 'user'
            self.content = request['user_request']

        if self.ds_type == 'assist_completion':
            self.ds_role = 'assistant'
            self.content = request['assistant_request']

        dataset = {"role": self.ds_role, "content": self.content}

        return dataset
'''
    def createAndSaveDataset(self, company_name, question, request):

        dataset = self.createDataset(company_name, question, request)

        return dataset
'''


class DatasetBuilder:

    def __init__(self):
        pass

    def createDatasetList(self, *args):

        ds_list = []
        for dataset in args:
            ds_list.append(dataset)

        return ds_list

    def createMessageTrainList(self, request):

        message_train_list = {'messages': request}

        return message_train_list

'''
    def createNewDataset(self, ds_type, request):

        newDataset = Dataset(ds_type, self.process_id).createAndSaveDataset(request)

        return newDataset

    def createDatasetFromTemplate(self, question, ds_type):

        request_template = {}

        if ds_type == 'system_request':
            request_template = SYSTEM_DATASET_TEMPLATE
            request_template['system_request'] =

        if ds_type == 'user_request':
            request_template = USER_DATASET_TEMPLATE
            request_template['user_request'] =

        return request_template

    def createCustomDataset(self, question, company_name, ds_type):

        request_template = {}

        if ds_type == 'system_request':
            request_template = SYSTEM_DATASET_TEMPLATE
            request_template['system_request'] = TRAIN_SYSTEM_REQUEST

        if ds_type == 'user_request':
            request_template = USER_DATASET_TEMPLATE
            request_template['user_request'] = TRAIN_USER_REQUEST.format(company_name) + question

        return request_template

    def createTrainDataset(self, request, ds_type):

        request_template = {}

        return request_template
'''





