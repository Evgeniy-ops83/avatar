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

    def createDataset(self, company_name, question='', **request):

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

