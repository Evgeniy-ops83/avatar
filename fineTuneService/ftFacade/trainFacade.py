from fineTuneService.ftModels.message import MessageListBuilder
from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftConfiguration.ftTrainConfig import message_template, question_list, system_message, user_message
from fineTuneService.ftFileManage.saveTrainDataset import saveTrainFile


def createNewTrain():

    for question in question_list:

        print(f'Next question is {question}')

        print('Creating request...')

        '''Create request for ChatGPT from template and question list'''
        message_template['system_request'] = system_message
        message_template['user_request'] = user_message + question

        '''Format template into completion message list (type = list)'''
        completion_request = MessageListBuilder().getMessageList(message_template)

        print('Sending request...')

        '''Send request to ChatGPT'''
        train_completion = ChatCompletion(completion_request).getCompletionJson()

        print('Saving train file...')

        '''Create row for train dataset'''
        train_ds = MessageListBuilder().getMessageTrainList(train_completion)

        saveTrainFile(train_ds)

        print(fr'Question {question} successfully added')

    return 'Train file successfully created'



a = createNewTrain()
print(a)