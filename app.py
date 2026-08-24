from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

from src.analytics import best_surf_times, get_beach_data, get_beach_forecast


DATA_FILE = Path(__file__).resolve().parent / "data" / "processed" / "surf_scores.csv"


def get_score_quality(score):
    if score >= 80:
        return "Excellent"
    if score >= 65:
        return "Good"
    if score >= 45:
        return "Fair"
    return "Poor"


st.title("Surf Forecast Analytics")

df = pd.read_csv(DATA_FILE)
df["time"] = pd.to_datetime(df["time"])

beach_name = st.sidebar.selectbox(
    "Surf Break",
    sorted(df["beach_name"].unique()),
)

beach_data = get_beach_data(df, beach_name).sort_values("time")
future_data = beach_data[beach_data["time"] >= datetime.now()]

if future_data.empty:
    st.warning("No future forecast data is available for this surf break.")
    st.stop()

next_forecast = future_data.iloc[0]
top_times = best_surf_times(future_data, beach_name, n=5)
best_time = top_times.iloc[0]

st.subheader("Next Forecast")
st.metric("Surf Score", f"{next_forecast['surf_score']:.1f}")
st.caption(
    f"{next_forecast['time']:%Y-%m-%d %H:%M} · "
    f"{get_score_quality(next_forecast['surf_score'])}"
)

st.subheader("Conditions")
wave_height, wave_period, wind_speed, swell_direction = st.columns(4)
wave_height.metric("Wave Height (m)", f"{next_forecast['wave_height']:.2f}")
wave_period.metric("Wave Period (s)", f"{next_forecast['wave_period']:.2f}")
wind_speed.metric("Wind Speed (km/h)", f"{next_forecast['wind_speed_10m']:.1f}")
swell_direction.metric("Swell Direction (°)", f"{next_forecast['wave_direction']:.0f}")

st.subheader("Best Time to Surf")
st.metric("Best Surf Score", f"{best_time['surf_score']:.1f}")
st.caption(f"{best_time['time']:%Y-%m-%d %H:%M}")

st.subheader("Top 5 Best Times")
st.dataframe(top_times, use_container_width=True)

st.subheader("Surf Score — 72 Hours")
st.line_chart(beach_data.set_index("time")["surf_score"])

st.subheader("72-Hour Forecast")
st.dataframe(get_beach_forecast(df, beach_name), use_container_width=True)
