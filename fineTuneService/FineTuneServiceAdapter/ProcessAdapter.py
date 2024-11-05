from ftConfiguration.ftTrainConfig import QUESTION_LIST, COMPANY_URL, FINE_TUNE_DATASET_DIR, FINE_TUNE_DATASET
from ftModels.FtProcess import FtProcess
from ftModels.FineTuneJob import FineTuneJob
from ftStorage.ftPgConnector import saveSourceObject


from flask import Flask

app = Flask(__name__)

@app.route('/start')
def hello_world():
    return 'Hello, world!'


@app.route('/process', methods=['POST'])
def do_something(question_list=QUESTION_LIST):

    newProcess = FtProcess()

    for question in question_list:

        request_completion = newProcess.createRequestFromTemplate(question)

        train_completion = newProcess.getTrainCompletion(request_completion)

        train_dataset = newProcess.createTrainDataset(train_completion)

        dataset_path = newProcess.saveDatasetFile(train_dataset)

    #saveSourceObject('process', newProcess.__dict__)

    return newProcess.__dict__

@app.route('/job', methods=['POST'])
def createJob(process_id='722133c6-8348-44c5-979b-73ab908c8d53', filename=FINE_TUNE_DATASET_DIR+FINE_TUNE_DATASET):

    NewJob = FineTuneJob(process_id)
    startNewJob = NewJob.createNewFinetuneJob(filename)
    request = {"filepath": FINE_TUNE_DATASET_DIR+filename}
    startNewJob = NewJob.createNewFinetuneJob(request)
    #saveSourceObject('ft_job', NewJob.__dict__)

    return NewJob.__dict__

@app.route('/save', methods=['POST'])
def hello_world():
    saveSourceObject()
    return 'saveSourceObject !'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



