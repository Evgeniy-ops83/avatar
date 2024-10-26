from fineTuneService.ftModels.message import MessageListBuilder
from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftConfiguration.ftTrainConfig import message_template, question_list, system_message, user_message


def createNewTrain():

    for question in question_list:

        message_template['system_request'] = system_message
        message_template['user_request'] = user_message + question

        completion_request = MessageListBuilder(message_template).message_list
        #print('completion_request - ', completion_request)
        #print(type(completion_request))

        train_completion = ChatCompletion(completion_request).getCompletion()

        train_ds = MessageListBuilder.getMessageTrainList(train_completion)
        print(train_ds)

    return 200



a = createNewTrain()
print(a)