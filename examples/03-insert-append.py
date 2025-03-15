import pandas as pd
from deltalake.writer import write_deltalake

# Change the import below to switch between S3 and HDFS
from config.s3_config import get_deltatable  # Use S3
# from config.hdfs_config import get_deltatable  # Use HDFS

data = {
    "id": [4, 5, 6],
    "name": ["David", "Eve", "Frank"],
    "age": [29, 33, 41],
    "region": ["US", "EU", "APAC"]
}
df = pd.DataFrame(data)

delta_table_path = get_deltatable().table_uri()

# Append new data
write_deltalake(delta_table_path, df, mode="append", partition_by=["region"])

print(f"✅ Data successfully appended to Delta table at: {delta_table_path}")
