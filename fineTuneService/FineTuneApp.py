from ftConfiguration.ftTrainConfig import QUESTION_LIST, COMPANY_URL, FINE_TUNE_DATASET_DIR, FINE_TUNE_DATASET
from ftModels.FtProcess import FtProcess
from ftModels.FineTuneJob import FineTuneJob
#from ftStorage.ftClickhouseConnector import saveSourceObject

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
#from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)
#api = Api(app)

@app.route('/start')
@cross_origin()
def hello_world():
    return 'Hello, world!'


@app.route('/process', methods=['POST'])
@cross_origin()
def createProcess(question_list=QUESTION_LIST):

    request_body = request.get_json()

    if request_body is None:
        company_name = COMPANY_URL
        print("error: No JSON data found")

    company_name = request_body.get("company_name")
    newProcess = FtProcess(company_name)

    for question in question_list:

        request_completion = (newProcess
                              .createRequestFromTemplate(question, company_name))
        train_completion = (newProcess
                            .getTrainCompletion(request_completion))
        train_dataset = (newProcess
                         .createTrainDataset(train_completion))
        dataset_path = (newProcess
                        .saveDatasetFile(train_dataset, company_name))

    #saveSourceObject('process', newProcess.__dict__)

    return newProcess.__dict__


@app.route('/job', methods=['POST'])
def createJob(process_id='722133c6-8348-44c5-979b-73ab908c8d53', filename=FINE_TUNE_DATASET_DIR+FINE_TUNE_DATASET):

    NewJob = FineTuneJob(process_id)
    request = {"filepath": FINE_TUNE_DATASET_DIR+filename}
    startNewJob = NewJob.createNewFinetuneJob(request)
    #saveSourceObject('ft_job', NewJob.__dict__)

    return NewJob.__dict__

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



