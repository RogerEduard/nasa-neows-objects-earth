import boto3
import pandas as pd
import io
import os
from dotenv import load_dotenv

# Load AWS credentials from .env
load_dotenv()
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

s3_client = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY,
                         aws_secret_access_key=AWS_SECRET_KEY
                        #,region_name='us-east-1'  # Cambia a tu región
                        )

#print  (s3_client.list_buckets())
#print("Archivo cargado exitosamente")

def upload_to_s3(bucket, key, dataframe):
    """Upload a DataFrame to AWS S3 in CSV format."""
    csv_buffer = io.StringIO()
    dataframe.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())
    print(f"File uploaded to S3: {key}")