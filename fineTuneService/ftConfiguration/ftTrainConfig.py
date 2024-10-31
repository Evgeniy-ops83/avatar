company_url = "coca-cola.com"
train_dataset_dir = rf'C:\Users\777\PycharmProjects\avatar\fineTuneService\resources\datasets\{company_url}'

train_filename = 'coca-cola.com - 2024-10-31'
train_filepath = rf'C:\Users\777\PycharmProjects\avatar\fineTuneService\resources\datasets\{train_filename}'
custom_model_suffix = 'avatar-model'

message_template = {
    'system_request': 'null',
    'user_request': 'null',
}

train_message_template = {
    "user_request": "null",
    "assistant_request": "null"
}

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
        Write the answer to the question in the format {train_message_template}, \
        Language English \
        Use JSON double quotes format in response and without any prefixes \
        where for the 'user_request', insert a question into the value, \
        and for the role 'assistant_request' insert your answer to the question into the value
        """

user_message = \
        f"""
        Write an answer to the question about the company based on the information on the {company_url} website:
        """


