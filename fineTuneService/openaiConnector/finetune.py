from fineTuneService.ftConfiguration.ftConfig import GENERAL_FT_MODEL
from fineTuneService.ftConfiguration.ftTrainConfig import FINE_TUNE_DATASET_DIR, FT_MODEL_SUFFIX

from openai import OpenAI
from pathlib import Path


class FineTune:

    def __init__(self, request):
        self.client = OpenAI()
        if 'filepath' in request.keys():
            self.filepath = Path(request['filepath'])
        else:
            self.filepath = Path(FINE_TUNE_DATASET_DIR)

        print('filepath - ', self.filepath)

        f = open(self.filepath)
        print(f.read())

    def createFinetuneFile(self):
        ft_file = self.client.files.create(
            file=open(self.filepath, "rb"),
            purpose="fine-tune"
        )
        return ft_file

    def createFinetuneJob(self, training_file, model=GENERAL_FT_MODEL):
        ft_job = self.client.fine_tuning.jobs.create(
            training_file=training_file,
            model=model,
            suffix=FT_MODEL_SUFFIX
        )
        return ft_job

    def getFinetuneJob(self, job_id):
        ft_job = self.client.fine_tuning.jobs.retrieve(job_id)
        return ft_job

