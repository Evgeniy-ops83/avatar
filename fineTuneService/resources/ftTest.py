from fineTuneService.openaiConnector.completion import ChatCompletion
from fineTuneService.ftModels.message import MessageBuilder

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


request = MessageBuilder(message)

print(request.message_list)
