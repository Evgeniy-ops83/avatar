from fineTuneService.ftConfiguration.ftTrainConfig import company_url, train_filepath
from fineTuneService.openaiConnector.finetune import FineTune

import time

def createNewFinetuneJob(request):

    if 'filepath' in request.keys():
        filepath = request
    else:
        filepath = train_filepath

    train_job = FineTune(filepath)

    train_file_id = train_job.createFinetuneFile().id
    print('train_file_id - ', train_file_id)

    train_ft_job_id = train_job.createFinetuneJob(train_file_id).id
    print('train_ft_job_id - ', train_ft_job_id)
    train_ft_job_status = train_job.getFinetuneJob(train_ft_job_id).status
    print('train_ft_job_status - ', train_ft_job_status)

    while train_ft_job_status != 'succeeded':
        train_ft_job_status = train_job.getFinetuneJob(train_ft_job_id).status
        print('Fine_tune is processing now. Please wait')
        print('train_ft_job_status - ', train_ft_job_status)
        time.sleep(5)

    ft_model = train_job.getFinetuneJob(train_ft_job_id).fine_tuned_model

    print(f'New model is {ft_model}')

    return 200


request = {'filepath': train_filepath}
a = createNewFinetuneJob(request)

