from src.nasa_api import get_neo_data
from src.aws_utils import upload_to_s3
from src.processing import process_neo_data
import pandas as pd

# Configuration
BUCKET_NAME = "objects-earth"
RAW_KEY = "raw-data/neo_data.csv"
PROCESSED_KEY = "processed-data/neo_processed.csv"

# Get data from NASA
print("Getting data from NASA...")
neo_data = get_neo_data(start_date="2025-01-01", end_date="2025-01-07")

# Save raw data to S3
df_raw = pd.DataFrame(neo_data)
#upload_to_s3(BUCKET_NAME, RAW_KEY, df_raw)

# Process data
df_processed = process_neo_data(neo_data)

# Load processed data to S3
upload_to_s3(BUCKET_NAME, PROCESSED_KEY, df_processed)

# Mostrar información clave
print("\nTop 5 objetos cercanos a la Tierra:")
print(df_processed.head())



