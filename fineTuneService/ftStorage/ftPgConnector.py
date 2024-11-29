from ftStorage.PgConnect import ConnectionBuilder
from ftConfiguration.ftConfig import DATASET_COLUMNS

pg_connect = ConnectionBuilder.pg_conn()


def saveObject(table, object):

    columns = DATASET_COLUMNS[table]

    with pg_connect.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"""
                INSERT INTO avatar_source.{table} ({columns}) VALUES (%s, %s, %s, %s, %s, %s)
                """,
                tuple(object.values())
            )
        conn.commit()

    return 'Object Saved'
