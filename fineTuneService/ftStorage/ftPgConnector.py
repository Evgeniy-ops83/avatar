from ftStorage.PgConnect import ConnectionBuilder
from ftConfiguration.ftConfig import COLUMNS

pg_connect = ConnectionBuilder.pg_conn()


def saveObjectDataset(object):

    columns = COLUMNS['dataset']

    with pg_connect.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"""
                INSERT INTO avatar_source.dataset ({columns}) VALUES (%s, %s, %s, %s, %s, %s)
                """,
                tuple(object.values())
            )
        conn.commit()

    return 'Object Saved'


def saveObjectFile(object):

    columns = COLUMNS['ds_file']

    with pg_connect.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"""
                INSERT INTO avatar_source.ds_file ({columns}) VALUES (%s, %s, %s, %s)
                """,
                tuple(object.values())
            )
        conn.commit()

    return 'Object Saved'


def saveObjectProcess(object):

    columns = COLUMNS['process']

    with pg_connect.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"""
                INSERT INTO avatar_source.process ({columns}) VALUES (%s, %s, %s, %s)
                """,
                tuple(object.values())
            )
        conn.commit()

    return 'Object Saved'