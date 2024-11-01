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

        print('Making the request...')  # Create request for ChatGPT from template and question list
        request = createRequestFromTemplate(question)
        print('request - ', request)

        # Format template into completion message list (type = list)
        completion_request = MessageListBuilder().getMessageList(request)
        print('completion_request - ', completion_request)

        print('Sending request...')  # Send request to ChatGPT
        train_completion = ChatCompletion(completion_request).getCompletionJson()
        print('train_completion - ', train_completion)

        print('Saving train file...')  # Create row for train dataset
        train_ds = MessageListBuilder().getMessageTrainList(train_completion)
        print('train_ds - ', train_ds)

        dataset_path = saveTrainFile(train_ds)  # Saving Train Dataset
        print('dataset_path - ', dataset_path)

        print(fr'Question {question} successfully added')

    return dataset_path


a = createNewTrainDataset()
print(a)
