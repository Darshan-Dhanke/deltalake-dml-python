import pandas as pd
from deltalake.writer import write_deltalake

# Change the import below to switch between S3 and HDFS
from config.s3_config import get_deltatable  # Use S3
# from config.hdfs_config import get_deltatable  # Use HDFS

data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "region": ["US", "EU", "US"]
}
dataframe = pd.DataFrame(data)

delta_table_path = get_deltatable().table_uri()

write_deltalake(delta_table_path, dataframe, mode="overwrite", partition_by=['region'])

print(f"✅ Data successfully overwritten in Delta table at: {delta_table_path}")