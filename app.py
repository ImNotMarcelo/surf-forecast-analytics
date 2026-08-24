from pathlib import Path

import pandas as pd
import streamlit as st

from src.analytics import best_surf_times, get_beach_data, get_beach_forecast


DATA_FILE = Path(__file__).resolve().parent / "data" / "processed" / "surf_scores.csv"


st.title("Surf Forecast Analytics")

df = pd.read_csv(DATA_FILE)
df["time"] = pd.to_datetime(df["time"])

beach_name = st.sidebar.selectbox(
    "Surf Break",
    sorted(df["beach_name"].unique()),
)

beach_data = get_beach_data(df, beach_name).sort_values("time")
next_forecast = beach_data.iloc[0]

st.metric("Surf Score", f"{next_forecast['surf_score']:.1f}")

st.dataframe(best_surf_times(df, beach_name, n=5), use_container_width=True)

st.line_chart(beach_data.set_index("time")["surf_score"])

st.dataframe(get_beach_forecast(df, beach_name), use_container_width=True)
