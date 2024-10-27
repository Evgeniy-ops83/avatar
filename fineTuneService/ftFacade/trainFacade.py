import json

from fineTuneService.ftModels.message import MessageListBuilder
from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftConfiguration.ftTrainConfig import message_template, question_list, system_message, user_message


def createNewTrain():

    for question in question_list:

        '''Create request for ChatGPT from template and question list'''
        message_template['system_request'] = system_message
        message_template['user_request'] = user_message + question

        '''Format template into completion message list (type = list)'''
        completion_request = MessageListBuilder().getMessageList(message_template)
        print('completion_request - ', completion_request)
        print(type(completion_request))

        '''Send request to ChatGPT'''
        train_completion = ChatCompletion(completion_request).getCompletionJson()
        print('train_completion - ', train_completion)
        print(type(train_completion))

        train_ds = MessageListBuilder().getMessageTrainList(train_completion)
        print('train_ds - ', train_ds)
        print(type(train_ds))

    return 200



a = createNewTrain()
print(a)