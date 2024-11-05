from ftStorage.PgConnect import ConnectionBuilder

Dataset = {
    'id': 'dwefwef',
    'ds_type': 'test',
    'process_id': 'test',
    'updated': 'test',
    'ds_role': 'test'
}

Columns = ('id', 'ds_type', 'process_id', 'updated', 'ds_role')

pg_connect = ConnectionBuilder.pg_conn()

with pg_connect.client().cursor() as cur:
    cur.execute(
        f"""
        INSERT INTO avatar_source.dataset ({Columns}) VALUES (%s),
        """,
        Dataset
    )
    obj = cur.fetchone()

    print(obj)