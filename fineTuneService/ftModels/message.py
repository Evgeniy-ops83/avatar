from fineTuneService.ftConfiguration.ftTrainConfig import TRAIN_REQUEST_TEMPLATE, TRAIN_SYSTEM_REQUEST, TRAIN_USER_REQUEST


class Message:
    def __init__(self, role, content):
        self.message = {"role": role, "content": content}


class MessageListBuilder:
    def __init__(self):
        self.message_list = []
        self.message_train_list = {}

    def createRequestFromTemplate(self, question):

        TRAIN_REQUEST_TEMPLATE['system_request'] = TRAIN_SYSTEM_REQUEST
        TRAIN_REQUEST_TEMPLATE['user_request'] = TRAIN_USER_REQUEST + question

        return TRAIN_REQUEST_TEMPLATE

    def getMessageList(self, request):

        if 'system_request' in request.keys():
            system_message = Message(role='system', content=request['system_request'])
            self.message_list.append(system_message.message)

        if 'user_request' in request.keys():
            user_message = Message(role='user', content=request['user_request'])
            self.message_list.append(user_message.message)

        if 'assistant_request' in request.keys():
            assistant_message = Message(role='assistant', content=request['assistant_request'])
            self.message_list.append(assistant_message.message)

        return self.message_list

    def getMessageTrainList(self, request):
        request = self.getMessageList(request)
        self.message_train_list['messages'] = request

        return self.message_train_list
