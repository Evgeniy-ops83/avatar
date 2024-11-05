import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
GENERAL_MODEL = "gpt-4o-mini"
GENERAL_FT_MODEL = "gpt-4o-mini-2024-07-18"

CH_DB_HOST = os.environ['CH_DB_HOST']
CH_DB_PORT = 9000

PG_DB_HOST = os.environ['PG_DB_HOST']
PG_DB_PORT = 5432
PG_DB_PW = os.environ['PG_DB_PW']

PG_CONNECTION = {
    'host': '146.185.208.30',
    'port': 5432,
    'db_name': 'av_assist',
    'user': 'asapp',
    'pw': PG_DB_PW
}
