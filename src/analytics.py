"""Reusable analytics helpers for surf forecast data."""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_FILE = BASE_DIR / "data" / "processed" / "surf_scores.csv"
BEACHES_FILE = BASE_DIR / "data" / "beaches.csv"


def get_beach_data(data, beach_name):
    """Return forecast data for the selected beach."""
    beach_data = data[data["beach_name"] == beach_name].copy()

    if beach_data.empty:
        raise ValueError(f"Beach not found: {beach_name}")

    return beach_data


def get_beach_config(beaches, beach_name):
    """Return configuration for the selected beach."""
    config = beaches[beaches["name"] == beach_name].copy()

    if config.empty:
        raise ValueError(f"Beach configuration not found: {beach_name}")

    return config.iloc[0]


def best_surf_times(data, beach_name, n=5):
    """Return the n forecast times with the highest Surf Score."""
    beach_data = get_beach_data(data, beach_name)

    columns = [
        "time",
        "surf_score",
        "wave_height",
        "wave_period",
        "wave_direction",
        "wind_speed_10m",
        "wind_direction_10m",
    ]

    return (
        beach_data[columns]
        .sort_values("surf_score", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )


def get_beach_forecast(data, beach_name):
    """Return the complete forecast table for the selected beach."""
    beach_data = get_beach_data(data, beach_name)

    columns = [
        "time",
        "surf_score",
        "wave_height",
        "wave_period",
        "wave_direction",
        "wind_speed_10m",
        "wind_direction_10m",
    ]

    return (
        beach_data[columns]
        .rename(
            columns={
                "time": "Time",
                "surf_score": "Surf Score",
                "wave_height": "Wave Height (m)",
                "wave_period": "Wave Period (s)",
                "wave_direction": "Swell Direction (°)",
                "wind_speed_10m": "Wind Speed (km/h)",
                "wind_direction_10m": "Wind Direction (°)",
            }
        )
        .reset_index(drop=True)
    )
