import pandas as pd

def process_neo_data(neo_data):
    """Processes NASA data and extracts key information."""
    all_asteroids = []
    
    for date, asteroids in neo_data["near_earth_objects"].items():
        for asteroid in asteroids:
            all_asteroids.append({
                "id": asteroid["id"],
                "name": asteroid["name"],
                "close_approach_date": date,
                "velocity_km_h": asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"],
                "diameter_km": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                "is_hazardous": asteroid["is_potentially_hazardous_asteroid"]
            })
    
    df = pd.DataFrame(all_asteroids)
    return df