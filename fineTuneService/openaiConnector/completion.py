from fineTuneService.ftConfiguration.ftConfig import GENERAL_MODEL

from openai import OpenAI
import json

class ChatCompletion:

    def __init__(self):
        self.client = OpenAI()
        self.model = GENERAL_MODEL

    def getCompletion(self, messages):

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return completion

    def getCompletionJson(self, **kwargs):

        completion = self.getCompletion(**kwargs)
        completion_json = json.dumps(f"{completion.choices[0].message.content}")

        return completion_json



