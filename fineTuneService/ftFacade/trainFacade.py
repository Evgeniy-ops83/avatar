from fineTuneService.ftModels.message import MessageListBuilder
from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftConfiguration.ftTrainConfig import TRAIN_REQUEST_TEMPLATE, QUESTION_LIST, TRAIN_SYSTEM_REQUEST, TRAIN_USER_REQUEST
from fineTuneService.ftFileManage.saveTrainDataset import saveTrainFile


def createRequestFromTemplate(question):

    TRAIN_REQUEST_TEMPLATE['system_request'] = TRAIN_SYSTEM_REQUEST
    TRAIN_REQUEST_TEMPLATE['user_request'] = TRAIN_USER_REQUEST + question

    return TRAIN_REQUEST_TEMPLATE

def createNewTrainDataset():

    for question in QUESTION_LIST:

        print(f'Next question is {question}')

        request = createRequestFromTemplate(question)  # Create request for ChatGPT from template and question list
        print('dataset request - ', request)

        completion_request = MessageListBuilder().getMessageList(request)  # Format request for Completion (list)
        print('completion_request - ', completion_request)

        train_completion = ChatCompletion(completion_request).getCompletionJson()  # Send request to ChatGPT
        print('train_completion - ', train_completion)

        train_ds = MessageListBuilder().getMessageTrainList(train_completion)  # Format GPT response for Train Dataset
        print('train_ds - ', train_ds)

        dataset_path = saveTrainFile(train_ds)  # Save Train Dataset
        print('dataset_path - ', dataset_path)

        print(fr'Question {question} successfully added')

    return 200

'''
a = createNewTrainDataset()
print(a)
'''