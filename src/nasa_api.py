import requests
import os
from dotenv import load_dotenv

# Cargar API Key desde .env
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

def get_neo_data(start_date, end_date):
    """Obtiene datos de objetos cercanos a la Tierra entre dos fechas."""
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={NASA_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.json()}")
        return None