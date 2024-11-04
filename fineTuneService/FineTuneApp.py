from ftConfiguration.ftTrainConfig import QUESTION_LIST, COMPANY_URL
from ftModels.FtProcess import FtProcess
#from ftStorage.ftClickhouseConnector import saveSourceObject

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/start')
def hello_world():
    return 'Hello, world!'


@app.route('/process', methods=['POST'])
def do_something(question_list=QUESTION_LIST):

    request_body = request.get_json()

    if request_body is None:
        company_name = COMPANY_URL
        print("error: No JSON data found")

    company_name = request_body.get("name")

    newProcess = FtProcess(company_name)

    for question in question_list:

        request_completion = newProcess.createRequestFromTemplate(question)

        train_completion = newProcess.getTrainCompletion(request_completion)

        train_dataset = newProcess.createTrainDataset(train_completion)

        dataset_path = newProcess.saveDatasetFile(train_dataset)

    #saveSourceObject('process', newProcess.__dict__)

    return newProcess.__dict__

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



