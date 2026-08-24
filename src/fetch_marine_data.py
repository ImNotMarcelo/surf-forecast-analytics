import requests
import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
BEACHES_FILE = BASE_DIR / "data" / "beaches.csv"
OUTPUT_FILE = BASE_DIR / "data" / "raw" / "marine_data.csv"

# Open-Meteo APIs
MARINE_API_URL = "https://marine-api.open-meteo.com/v1/marine"
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_marine_data():
    """Fetch marine and weather forecasts and save the raw dataset."""
    # Load beaches
    beaches = pd.read_csv(BEACHES_FILE)

    all_data = []

    for _, beach in beaches.iterrows():

        print(f"Fetching data for {beach['name']}...")

        # -----------------------------
        # Marine data
        # -----------------------------
        marine_params = {
            "latitude": beach["latitude"],
            "longitude": beach["longitude"],
            "hourly": ",".join([
                "wave_height",
                "wave_period",
                "wave_direction",
                "wind_wave_height",
                "swell_wave_height",
                "swell_wave_period",
                "swell_wave_direction",
            ]),
            "timezone": "America/Lima",
            "forecast_days": 3,
        }

        marine_response = requests.get(
            MARINE_API_URL,
            params=marine_params,
            timeout=30
        )

        marine_response.raise_for_status()

        marine_data = marine_response.json()

        marine_hourly = pd.DataFrame(marine_data["hourly"])

        # -----------------------------
        # Weather data
        # -----------------------------
        weather_params = {
            "latitude": beach["latitude"],
            "longitude": beach["longitude"],
            "hourly": "wind_speed_10m,wind_direction_10m",
            "timezone": "America/Lima",
            "forecast_days": 3,
        }

        weather_response = requests.get(
            WEATHER_API_URL,
            params=weather_params,
            timeout=30
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        weather_hourly = pd.DataFrame(weather_data["hourly"])

        # -----------------------------
        # Merge marine + weather
        # -----------------------------
        hourly = marine_hourly.merge(
            weather_hourly,
            on="time",
            how="left"
        )

        hourly["beach_id"] = beach["id"]
        hourly["beach_name"] = beach["name"]

        all_data.append(hourly)

    # Combine all beaches
    marine_data = pd.concat(all_data, ignore_index=True)

    # Save
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    marine_data.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print()
    print(f"Saved {len(marine_data)} rows to:")
    print(OUTPUT_FILE)

    return marine_data


if __name__ == "__main__":
    fetch_marine_data()
