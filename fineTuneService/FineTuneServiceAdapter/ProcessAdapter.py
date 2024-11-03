from fineTuneService.ftConfiguration.ftTrainConfig import QUESTION_LIST
from fineTuneService.ftModels.FtProcess import FtProcess
from fineTuneService.ftStorage.ftClickhouseConnector import saveSourceObject

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

    saveSourceObject('process', newProcess.__dict__)

    return newProcess.__dict__

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



