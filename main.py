from src.nasa_api import get_nasa_products
from src.processing import process_nasa_data, analyze_nasa_data
from src.aws_utils import upload_to_s3
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from file .env
load_dotenv()

# Configuration
API_KEY = os.getenv("NASA_API_KEY")  # Load the API Key from the .env
BUCKET_NAME = "objects-earth"
RAW_KEY = "raw-data/nasa_products.csv"
PROCESSED_KEY = "processed-data/nasa_processed.csv"



