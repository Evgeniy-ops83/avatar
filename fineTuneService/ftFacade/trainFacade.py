from fineTuneService.ftModels.message import MessageListBuilder
from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftConfiguration.ftTrainConfig import message_template, question_list, system_message, user_message
from fineTuneService.ftFileManage.saveTrainDataset import saveTrainFile


def createRequestFromTemplate(question):

    message_template['system_request'] = system_message
    message_template['user_request'] = user_message + question

    return message_template

def createNewTrainDataset():

    for question in question_list:

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
