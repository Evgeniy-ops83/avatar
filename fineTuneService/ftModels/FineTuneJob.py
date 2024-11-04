from ftConfiguration.ftConfig import GENERAL_FT_MODEL
from ftConfiguration.ftTrainConfig import COMPANY_URL, FINE_TUNE_DATASET_DIR, FINE_TUNE_DATASET
from openaiConnector.finetune import FineTune
#from ftStorage.ftClickhouseConnector import saveSourceObject
from ftFileManage.CreatePath import createDir

import time
from datetime import datetime
import uuid


class FineTuneJob:
    id: str
    key: str
    process_id: str
    error: str
    ft_status: str
    general_model: str
    ft_model: str
    ft_file_id: str
    created: str

    def __init__(self, process_id):
        self.id = str(uuid.uuid4())
        self.key = 'undefined'
        self.process_id = process_id
        self.error = 'undefined'
        self.ft_status = 'undefined'
        self.general_model = GENERAL_FT_MODEL
        self.ft_model = 'undefined'
        self.ft_file_id = 'undefined'
        self.created = str(datetime.now())

    def createNewFinetuneJob(self, request):

        if 'filename' in request.keys():
            filepath = createDir(request['filepath'])
        else:
            filepath = createDir(FINE_TUNE_DATASET_DIR)

        ft_job = FineTune(filepath)

        self.ft_file_id = ft_job.createFinetuneFile().id
        print('ft_file_id - ', self.ft_file_id)

        self.key = ft_job.createFinetuneJob(self.ft_file_id).id
        print('train_ft_job_id - ', self.key)

        print('Fine tune is in process now. Please wait')
        self.ft_status = ft_job.getFinetuneJob(self.key).status
        print('train_ft_job_status - ', self.ft_status)

        while self.ft_status not in ['succeeded', 'failed']:

            train_ft_job_info = ft_job.getFinetuneJob(self.key)

            if train_ft_job_info.status != self.ft_status:
                self.ft_status = train_ft_job_info.status
                print('train_ft_job_status - ', self.ft_status)

            if self.ft_status == 'succeeded':
                self.ft_model = train_ft_job_info.fine_tuned_model

            time.sleep(15)

        print(f'Training successfully finished for job {self.key}')

        return 200


'''
newJobRequest = {'filename': FINE_TUNE_DATASET_DIR+FINE_TUNE_DATASET}
NewJob = FineTuneJob('ceef0ceb-9bc8-4c55-92f7-435488393cac')
startNewJob = NewJob.createNewFinetuneJob(newJobRequest)
saveSourceObject('ft_job', NewJob.__dict__)
'''

