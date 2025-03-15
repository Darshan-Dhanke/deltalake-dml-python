import os
from deltalake import DeltaTable

def get_deltatable():
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    LOCATION = os.getenv("AWS_REGION")
    S3_BUCKET = os.getenv("S3_BUCKET")
    PREFIX = os.getenv("S3_PREFIX")

    PATH = f's3://{S3_BUCKET}{PREFIX}'
    storage_options = {"AWS_REGION": LOCATION}

    return DeltaTable(PATH, storage_options=storage_options)
