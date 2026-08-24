"""Build the processed surf forecast dataset from raw forecast data."""

from pathlib import Path

import pandas as pd

from surf_score import calculate_surf_score


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_FILE = BASE_DIR / "data" / "raw" / "marine_data.csv"
BEACHES_FILE = BASE_DIR / "data" / "beaches.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "surf_scores.csv"


def process_data():
    """Calculate Surf Scores and save the processed forecast dataset."""
    marine_data = pd.read_csv(RAW_DATA_FILE)
    beaches = pd.read_csv(BEACHES_FILE).rename(columns={"id": "beach_id"})

    processed_data = marine_data.merge(
        beaches[
            [
                "beach_id",
                "preferred_swell_direction_deg",
                "swell_direction_tolerance_deg",
                "preferred_wind_direction_deg",
                "wind_direction_tolerance_deg",
            ]
        ],
        on="beach_id",
        how="left",
    )

    processed_data["surf_score"] = processed_data.apply(
        lambda row: calculate_surf_score(
            wave_height=row["wave_height"],
            wave_period=row["wave_period"],
            wind_speed=row["wind_speed_10m"],
            wave_direction=row["wave_direction"],
            preferred_swell_direction=row["preferred_swell_direction_deg"],
            wind_direction=row["wind_direction_10m"],
            preferred_wind_direction=row["preferred_wind_direction_deg"],
        ),
        axis=1,
    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    processed_data.to_csv(OUTPUT_FILE, index=False)

    return processed_data


if __name__ == "__main__":
    data = process_data()
    print(f"Saved {len(data)} rows to: {OUTPUT_FILE}")
