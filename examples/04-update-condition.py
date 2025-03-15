import pandas as pd
from deltalake.writer import write_deltalake

# Change the import below to switch between S3 and HDFS
from config.s3_config import get_deltatable  # Use S3
# from config.hdfs_config import get_deltatable  # Use HDFS

delta_table = get_deltatable()
delta_table_path = delta_table.table_uri()

delta_table.delete("id = 4")

update_df = pd.DataFrame({
    "id": [4],
    "name": ["David"],
    "age": [32],
    "region": ["US"]
})

write_deltalake(delta_table_path, update_df, mode='append', partition_by=["region"])

print(f"✅ Conditional-based update completed in Delta table at: {delta_table_path}")
