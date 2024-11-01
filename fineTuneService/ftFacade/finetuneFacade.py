from fineTuneService.ftConfiguration.ftTrainConfig import COMPANY_URL, FINE_TUNE_DATASET_DIR
from fineTuneService.openaiConnector.finetune import FineTune

import time

def createNewFinetuneJob(request):

    if 'filepath' in request.keys():
        filepath = request
    else:
        filepath = FINE_TUNE_DATASET_DIR

    train_job = FineTune(filepath)

    train_file_id = train_job.createFinetuneFile().id
    print('train_file_id - ', train_file_id)

    train_ft_job_id = train_job.createFinetuneJob(train_file_id).id
    print('train_ft_job_id - ', train_ft_job_id)
    train_ft_job_status = train_job.getFinetuneJob(train_ft_job_id).status
    print('train_ft_job_status - ', train_ft_job_status)

    print('Fine tune is in process now. Please wait')
    train_ft_job_status = train_job.getFinetuneJob(train_ft_job_id).status
    print('train_ft_job_status - ', train_ft_job_status)

    while train_ft_job_status != 'succeeded':

        train_ft_job_info = train_job.getFinetuneJob(train_ft_job_id)
        new_train_ft_job_status = train_ft_job_info.status

        if new_train_ft_job_status != train_ft_job_status:
            print('train_ft_job_status - ', new_train_ft_job_status)

        if new_train_ft_job_status == 'failed':
            raise TypeError(f"Error occurred while fine tuning: {train_ft_job_info.error}")

        time.sleep(15)

    ft_model = train_job.getFinetuneJob(train_ft_job_id).fine_tuned_model

    print(f'New model is {ft_model}')

    return 200


request = {'filepath': FINE_TUNE_DATASET_DIR}
a = createNewFinetuneJob(request)

