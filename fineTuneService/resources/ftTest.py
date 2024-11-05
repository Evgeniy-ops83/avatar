from fineTuneService.ftStorage.ftPgConnector import ConnectionBuilder



pg_connect = ConnectionBuilder.pg_conn()

with pg_connect.client().cursor() as cur:
    cur.execute(
        """
        SELECT version();
        """
    )
    obj = cur.fetchone()

    print(obj)