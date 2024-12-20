import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
GENERAL_MODEL = "gpt-4o-mini"
GENERAL_FT_MODEL = "gpt-4o-mini-2024-07-18"

BASIC_URL = os.environ['BASIC_URL']

CH_DB_HOST = BASIC_URL
CH_DB_PORT = 9000

PG_DB_HOST = BASIC_URL
PG_DB_PORT = 5432
PG_DB_PW = os.environ['PG_DB_PW']

PG_CONNECTION = {
    'host': BASIC_URL,
    'port': 5432,
    'db_name': 'av_assist',
    'user': 'asapp',
    'pw': PG_DB_PW
}

COLUMNS = {
    'dataset': 'id, ds_type, process_id, updated, ds_role, content',
    'process': 'id, company_url, created',
    'ds_file': 'id, process_id, filename, created',
    'ft_job': 'key, process_id, ft_status, general_model, ft_model, ft_file_id, error, created'
}

DATASET_COLUMNS = 'id, ds_type, process_id, updated, ds_role, content'


