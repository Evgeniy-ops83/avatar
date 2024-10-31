company_url = "coca-cola.com"
train_dataset_dir = rf'C:\Users\777\PycharmProjects\avatar\fineTuneService\resources\datasets\{company_url}'

train_filename = 'coca-cola.com - 2024-10-31'
train_filepath = rf'C:\Users\777\PycharmProjects\avatar\fineTuneService\resources\datasets\{train_filename}'
custom_model_suffix = 'avatar-model'

system_message_template = {"role": "system", "content": "null"}
user_message_template = {"role": "user", "content": "null"}
assistant_message_template = {"role": "assistant", "content": "null"}

question_list = [
    'What is the name of the company?',
    'What is the advertising description of the company ?',
    'What are the categories of products or services offered by the company ?'
]

system_message = \
        f"""
        Write the answer to the question, \
        Language English \
        Use JSON format in response with double quotes and without any prefixes \
        Use {user_message_template} where for the 'user' role, insert a question into the 'content' value, \
        Use {assistant_message_template}, where for the 'assistant' role insert your answer into the 'content' value
        """

user_message = \
        f"""
        Write an answer to the question about the company based on the information on the {company_url} website:
        """


