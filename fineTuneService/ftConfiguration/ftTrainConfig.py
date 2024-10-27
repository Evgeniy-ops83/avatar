company_url = "coca-cola.com"
train_dataset_dir = rf'C:\Users\777\PycharmProjects\avatar\fineTuneService\resources\datasets\{company_url}'

message_template = {
    'system_request': 'null',
    'user_request': 'null',
}

train_message_template = {
    "user_request": "null",
    "assistant_request": "null"
}

question_list = [
    'What is the name of the company?',
    'What is the advertising description of the company ?',
    'What are the categories of products or services offered by the company ?'
]

system_message = \
        f"""
        Write the answer to the question in the format {train_message_template}, \
        Language English \
        Write JSON format in response with double quotes and without any prefixes \
        where for the 'user_request', insert a question into the value, \
        and for the role 'assistant_request' insert your answer to the question into the value
        """

user_message = \
        f"""
        Write an answer to the question about the company based on the information on the {company_url} website:
        """


