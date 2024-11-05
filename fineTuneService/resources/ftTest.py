from fineTuneService.ftStorage.ftPgConnector import ConnectionBuilder


pg_connect = ConnectionBuilder.pg_conn()

with pg_connect.connection() as conn:
    conn.execute(
        """
        SELECT version();
        """
    )
    obj = conn.fetchone()

    print(obj)