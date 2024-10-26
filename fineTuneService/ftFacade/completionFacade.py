from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftModels.message import MessageListBuilder



system_request = 'Write response in official style'
user_request = 'Hello'
assistant_request = 'Hello Mr.'

message = {
    'system_request': system_request,
    'user_request': user_request
}

message_train = {
    'system_request': system_request,
    'user_request': user_request,
    'assistant_request': assistant_request
}


#messages = MessageListBuilder(message).message_list
train_dict = MessageListBuilder(message).getMessageTrainList()
#completion = ChatCompletion(messages).getCompletion()
print(train_dict)