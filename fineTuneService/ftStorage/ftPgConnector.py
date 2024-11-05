from ftStorage.PgConnect import ConnectionBuilder
import json

Dataset = {
    'id': '28f10a42-b5c4-4ec5-960c-02f66af51759',
    'ds_type': 'test',
    'process_id': 'test',
    'updated': 'test',
    'ds_role': 'test',
    'content': 'test'
}

Columns = 'id, ds_type, process_id, updated, ds_role, content'


pg_connect = ConnectionBuilder.pg_conn()

def saveSourceObject():

    with pg_connect.connection().cursor() as cur:
        cur.execute(
            f"""
            INSERT INTO avatar_source.dataset ({Columns}) VALUES (%s, %s, %s, %s, %s, %s)
            """,
            tuple(Dataset.values())
        )

    return 'Object Saved'


'''
    with pg_connect.client().cursor() as cur:
        cur.execute(
            f"""
            INSERT INTO avatar_source.dataset ({Columns}) VALUES (%s, %s, %s, %s, %s, %s)
            """,
            tuple(Dataset.values())
        )
'''