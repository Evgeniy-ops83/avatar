from ftConfiguration.ftConfig import CH_DB_HOST, CH_DB_PORT
from clickhouse_driver import Client
import json
import pandas as pd
import numpy as np

client = Client(host=CH_DB_HOST, port=CH_DB_PORT, settings={'use_numpy': True})


def saveSourceObject(type, object):

    client.execute(f" INSERT INTO avatar_source.{type} FORMAT JSONEachRow {json.dumps(object)}",
                   )
    return 'OK'

