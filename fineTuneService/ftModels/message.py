

class Message:
    def __init__(self, role, content):
        self.message = {"role": role, "content": content}


class MessageBuilder:
    def __init__(self, request):
        self.message_list = []
        self.message_train_list = {'messages': []}

        if 'system_request' in request.keys():
            self.system_message = Message(role='system', content=request['system_request'])

        if 'user_request' in request.keys():
            self.user_message = Message(role='user', content=request['user_request'])

        if 'assistant_request' in request.keys():
            self.assistant_message = Message(role='assist', content=request['assistant_request'])

    def getMessageList(self):
        self.message_list.append(self.system_message.message)
        self.message_list.append(self.user_message.message)
        self.message_list.append(self.system_message.message)

        return self.message_list

    def getMessageTrainList(self):
        self.message_train_list['messages'].append(self.system_message.message)
        self.message_train_list['messages'].append(self.user_message.message)
        self.message_train_list['messages'].append(self.assistant_message.message)

        return self.message_train_list
