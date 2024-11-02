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

        # Format template into completion message list (type = list)
        completion_request = MessageListBuilder().getMessageList(request)

        print('Sending request...')  # Send request to ChatGPT
        train_completion = ChatCompletion(completion_request).getCompletionJson()

        print('Saving train file...')  # Create row for train dataset
        train_ds = MessageListBuilder().getMessageTrainList(train_completion)

        dataset_path = saveTrainFile(train_ds)  # Saving Train Dataset

        print(fr'Question {question} successfully added')

    return f'Train file successfully created in {dataset_path}'


a = createNewTrainDataset()
print(a)
