from fineTuneService.ftConfiguration.ftConfig import GENERAL_MODEL

from openai import OpenAI
import json

class ChatCompletion:

    def __init__(self, messages):
        self.client = OpenAI()
        self.model = GENERAL_MODEL
        self.messages = messages

    def getCompletion(self):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        response = completion.choices[0].message.content

        return response

    def getCompletionJson(self):

        completion = self.getCompletion()
        print('completion - ', completion)
        completion_json = json.loads(completion)

        return completion_json



