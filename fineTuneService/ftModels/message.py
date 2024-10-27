

class Message:
    def __init__(self, role, content):
        self.message = {"role": role, "content": content}


class MessageListBuilder:
    def __init__(self):
        self.message_list = []
        self.message_train_list = {"messages": []}

    def getMessageList(self, request):

        if 'system_request' in request.keys():
            self.system_message = Message(role='system', content=request['system_request'])
            self.message_list.append(self.system_message.message)

        if 'user_request' in request.keys():
            self.user_message = Message(role='user', content=request['user_request'])
            self.message_list.append(self.user_message.message)

        if 'assistant_request' in request.keys():
            self.assistant_message = Message(role='assist', content=request['assistant_request'])
            self.message_list.append(self.system_message.message)

        return self.message_list

    def getMessageTrainList(self, request):
        self.message_train_list['messages'].append(request)

        return self.message_train_list
