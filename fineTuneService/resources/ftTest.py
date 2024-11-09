TRAIN_SYSTEM_REQUEST = \
        {
            'role': 'system',
            'content': 'Write the answer to the question in the format {}, Language English'
        }

USER_REQUEST = \
    {
        'role': 'user',
        'content': 'Write an answer to the question about the company based on the information on the elevenlabs.io website: \
    What is the name of the company?'
    }

a = [TRAIN_SYSTEM_REQUEST, USER_REQUEST]

print(a)
