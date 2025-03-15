from datetime import datetime, timezone

# Change the import below to switch between S3 and HDFS
from config.s3_config import get_deltatable  # Use S3
# from config.hdfs_config import get_deltatable  # Use HDFS

delta_table = get_deltatable()

for entry in delta_table.history():
    print({
        'version': entry['version'],
        'operation': entry['operation'],
        'timestamp': datetime.fromtimestamp(entry['timestamp'] / 1000, tz=timezone.utc),
        'num_added_files': 0 if 'num_added_files' not in entry['operationMetrics'] else entry['operationMetrics']['num_added_files'],
        'num_added_rows': 0 if 'num_added_rows' not in entry['operationMetrics'] else entry['operationMetrics']['num_added_rows'],
        'num_removed_files': 0 if 'num_removed_files' not in entry['operationMetrics'] else entry['operationMetrics']['num_removed_files']
    })
