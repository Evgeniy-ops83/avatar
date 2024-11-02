from fineTuneService.ftConfiguration.ftTrainConfig import SYSTEM_DATASET_TEMPLATE, USER_DATASET_TEMPLATE, TRAIN_SYSTEM_REQUEST, TRAIN_USER_REQUEST, ASSIST_DATASET_TEMPLATE

from pydantic import BaseModel
import uuid
from datetime import datetime


class DatasetBuilder:

    def createDatasetFromTemplate(self, question, ds_type):

        request_template = {}

        if ds_type == 'system_request':
            request_template = SYSTEM_DATASET_TEMPLATE
            request_template['system_request'] = TRAIN_SYSTEM_REQUEST

        if ds_type == 'user_request':
            request_template = USER_DATASET_TEMPLATE
            request_template['user_request'] = TRAIN_USER_REQUEST + question

        return request_template

    def createTrainDataset(self, ds_type, request):

        request_template = {}

        if ds_type == 'user_completion':
            request_template = USER_DATASET_TEMPLATE
            request_template['user_request'] = request

        if ds_type == 'assist_completion':
            request_template = ASSIST_DATASET_TEMPLATE
            request_template['assistant_request'] = request

        return request_template

    def createDatasetList(self, *args):

        ds_list = []
        for dataset in args:
            ds_list.append(dataset)

        return ds_list

    def createMessageTrainList(self, request):

        message_train_list = {'messages': request}

        return message_train_list


class Dataset:
    ID: str
    TYPE: str
    PROCESS_ID: str
    UPDATED: str
    ROLE: str
    CONTENT: str

    def __init__(self, ds_type, process_id):
        self.ID = str(uuid.uuid4())
        self.TYPE = ds_type
        self.PROCESS_ID = process_id
        self.UPDATED = str(datetime.now())
        self.ROLE = 'undefined'
        self.CONTENT = 'undefined'

    def createDataset(self, request):

        if 'system_request' in request.keys():
            self.ROLE = 'system'
            self.CONTENT = request['system_request']
        elif 'user_request' in request.keys():
            self.ROLE = 'user'
            self.CONTENT = request['user_request']
        elif 'assistant_request' in request.keys():
            self.ROLE = 'assistant'
            self.CONTENT = request['assistant_request']

        dataset = {"role": self.ROLE, "content": self.CONTENT}

        return dataset

