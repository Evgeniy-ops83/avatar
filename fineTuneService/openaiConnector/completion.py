from ftConfiguration.ftConfig import GENERAL_MODEL

import openai
import json

class ChatCompletion:

    def __init__(self, messages):
        self.client = openai
        self.model = GENERAL_MODEL
        self.messages = messages

    def getCompletion(self):
        completion = self.client.Completion.create(
            model=self.model,
            messages=self.messages
        )
        response = completion.choices[0].message.content

        return response

    def getCompletionJson(self):

        completion = self.getCompletion()
        completion_json = json.loads(completion)

        return completion_json



