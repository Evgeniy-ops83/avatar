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

