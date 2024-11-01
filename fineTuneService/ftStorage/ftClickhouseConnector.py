from fineTuneService.ftConfiguration.ftConfig import CH_DB_HOST, CH_DB_PORT

from clickhouse_driver import Client

client = Client(host=CH_DB_HOST, port=CH_DB_PORT, settings={'use_numpy': True})

def saveJSONEntity(value):

    client.execute(f" INSERT INTO ml_db_001.lin_reg_pred_2023_11_01 (predicted_price) VALUES ({value}) ",
                   )

    return 'OK'

