

class Message:
    def __init__(self, role, content):
        self.message = {"role": role, "content": content}


class MessageListBuilder:
    def __init__(self, request):
        self.message_list = []
        self.message_train_list = {'messages': []}

        if 'system_request' in request.keys():
            self.system_message = Message(role='system', content=request['system_request'])
            self.message_list.append(self.system_message.message)

        if 'user_request' in request.keys():
            self.user_message = Message(role='user', content=request['user_request'])
            self.message_list.append(self.user_message.message)

        if 'assistant_request' in request.keys():
            self.assistant_message = Message(role='assist', content=request['assistant_request'])
            self.message_list.append(self.system_message.message)

    def getMessageTrainList(self):
        self.message_train_list['messages'] = self.message_list

        return self.message_train_list
