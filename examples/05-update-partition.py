import pandas as pd
from deltalake.writer import write_deltalake

# Change the import below to switch between S3 and HDFS
from config.s3_config import get_deltatable  # Use S3
# from config.hdfs_config import get_deltatable  # Use HDFS

delta_table = get_deltatable()
delta_table_path = delta_table.table_uri()

update_df = pd.DataFrame(update_data = {
    "id": [2, 5],
    "name": ["Bob Updated", "Eve Updated"],
    "age": [32, 35],
    "region": ["EU", "EU"]
})
partition_filters = [{'region', '=', 'EU'}]

write_deltalake(delta_table_path,
    update_df,
    mode='overwrite',
    partition_by=["region"],
    partition_filters=partition_filters,
    engine='rust'
    )

print(f"✅ Partition-based update completed in Delta table at: {delta_table_path}")
