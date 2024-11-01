"""CREATING TRAIN DATASET"""

COMPANY_URL = "snickers.com"  # for API

# create various questions templates for different business types
QUESTION_LIST = [
    'What is the name of the company?',
    'What is the advertising description of the company ?',
    'What are the categories of products or services offered by the company ?',
    'What is the foundation history of the company ? (use around 100 symbols in response)',
    'What is the key persons in company?',
    'What is the mission of the company in one sentence ?',
    'List 3 last events in which company was participated lately ?',
    'How can I buy company products ?',
    'How can I get delivery of company products ?',
    'What is the key feedback points about the company from customers ? (use around 100 symbols in response)'
]
TRAIN_REQUEST_TEMPLATE = {
    'system_request': 'null',
    'user_request': 'null',
}
TRAIN_DATASET_FORMAT = {
    "user_request": "null",
    "assistant_request": "null"
}
TRAIN_SYSTEM_REQUEST = \
        f"""
        Write the answer to the question in the format {TRAIN_DATASET_FORMAT}, \
        Language English \
        Use JSON double quotes format in response and without any prefixes \
        where for the 'user_request', insert a question into the value, \
        and for the role 'assistant_request' insert your answer to the question into the value
        """
TRAIN_USER_REQUEST = \
        f"""
        Write an answer to the question about the company based on the information on the {COMPANY_URL} website:
        """
DATASET_SAVE_DIR = rf'C:\Users\777\PycharmProjects\avatar\fineTuneService\resources\datasets\{COMPANY_URL}'

"""CREATING FINE TUNE JOB"""

FINE_TUNE_DATASET = 'snickers.com - 2024-11-01'
FT_MODEL_SUFFIX = 'avatar-model'    # for API
FINE_TUNE_DATASET_DIR = rf'C:\Users\777\PycharmProjects\avatar\fineTuneService\resources\datasets\{FINE_TUNE_DATASET}'


