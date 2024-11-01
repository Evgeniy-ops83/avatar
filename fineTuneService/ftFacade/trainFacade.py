from fineTuneService.ftModels.message import MessageListBuilder
from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftConfiguration.ftTrainConfig import QUESTION_LIST
from fineTuneService.ftFileManage.saveTrainDataset import saveTrainFile


def createNewTrainDataset():

    for question in QUESTION_LIST:

        print(f'Next question is {question}')

        input_request = MessageListBuilder()  # Create request for ChatGPT from template
        request = input_request.createRequestFromTemplate(question)
        completion_request = input_request.getMessageList(request)
        print('completion_request - ', completion_request)

        completion_response = ChatCompletion(completion_request).getCompletionJson()  # Send request to ChatGPT
        print('train_completion - ', completion_response)

        response = MessageListBuilder()  # Format GPT response for Train Dataset
        response_object = response.getMessageList(completion_response)
        response_dataset = response.getMessageTrainList(response_object)
        print('response_dataset - ', response_dataset)

        dataset_path = saveTrainFile(response_dataset)  # Save Train Dataset
        print('dataset_path - ', dataset_path)

        print(fr'Question {question} successfully added')

    return 200


a = createNewTrainDataset()
print(a)
