# Change the import below to switch between S3 and HDFS
from config.s3_config import get_deltatable  # Use S3
# from config.hdfs_config import get_deltatable  # Use HDFS

delta_table = get_deltatable()
delta_table_path = delta_table.table_uri()

delta_table.delete("id = 4")

print(f"✅ Condition-based delete completed in Delta table at: {delta_table_path}")