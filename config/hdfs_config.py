import os
from deltalake import DeltaTable

def get_deltatable():
    HDFS_URI = os.getenv("HDFS_URI")
    PREFIX = os.getenv("HDFS_PREFIX")

    PATH = f'hdfs://{HDFS_URI}{PREFIX}'
    return DeltaTable(PATH).table_uri
