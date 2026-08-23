# 🏄 Surf Forecast Analytics

An open-source data analytics project that transforms marine and weather forecast data into an interpretable **Surf Score (0–100)** for multiple surf breaks.

The goal is to combine programming, data analysis, APIs and domain knowledge to answer a simple question:

> **Where and when are the best conditions to surf?**

---

## 🌊 Project Overview

Surf conditions depend on multiple variables. Wave height alone is not enough to determine whether conditions are good.

This project combines:

- 🌊 Wave height
- ⏱️ Wave period
- 🧭 Swell direction
- 💨 Wind speed
- 🧭 Wind direction

These variables are combined into an experimental Surf Score from **0 to 100**.

The project currently analyzes **10 surf breaks in Peru**:

1. Máncora
2. Lobitos
3. Chicama
4. Huanchaco
5. Pacasmayo
6. Punta Roquitas
7. Punta Hermosa
8. Punta Rocas
9. San Bartolo
10. Cerro Azul

---

## 🧠 Surf Score Model

The current model uses five components:

| Factor | Weight |
|---|---:|
| Wave height | 25% |
| Wave period | 25% |
| Wind speed | 15% |
| Swell direction | 15% |
| Wind direction | 20% |
| **Total** | **100%** |

Each component is converted into a score between 0 and 100.

The final score is calculated as a weighted combination of these components.

> **Important:** The Surf Score is an experimental and configurable model. It is not intended to represent a universal or scientifically validated measure of surf quality.

---

## 📊 Current Features

The project currently supports:

- Marine forecast data collection
- Weather forecast data collection
- Data cleaning and preparation
- Exploratory Data Analysis
- Surf Score calculation
- Surf break ranking
- 72-hour forecast analysis
- Best surf time identification
- Hourly condition analysis
- Interactive surf break selection in Jupyter

---

## 🔄 Data Pipeline
```text
Surf Break Coordinates
        ↓
Open-Meteo Marine API
        +
Open-Meteo Weather API
        ↓
Raw Forecast Data
        ↓
Data Processing
        ↓
Surf Score Model
        ↓
Processed Dataset
        ↓
Analysis & Visualization
```

---

## 🗂️ Project Structure

surf-forecast-analytics/
│
├── data/
│   ├── raw/
│   │   └── marine_data.csv
│   │
│   ├── processed/
│   │   └── surf_scores.csv
│   │
│   └── beaches.csv
│
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
│
├── src/
│   ├── fetch_marine_data.py
│   └── surf_score.py
│
├── .gitignore
├── README.md
└── requirements.txt

---

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Requests
- Git
- GitHub
- Open-Meteo APIs

---

## 🚀 Project Status

Current
- Git repository
- Python environment
- Initial surf break dataset
- Marine API integration
- Weather API integration
- Exploratory analysis
- Surf Score model
- 72-hour forecast
- Surf break ranking
- Best surf time analysis

Future
- Improve break-specific parameters
- Validate the Surf Score against real surf conditions
- Add tide data
- Improve wind direction modeling
- Historical data analysis
- Forecast accuracy evaluation
- Machine learning experiments
- Interactive web dashboard
- Support for international surf breaks
- Automated data updates

---

## 📚 Learning Goals

This project is also a personal learning project focused on developing practical skills in:

- Python programming
- Data analysis
- Data visualization
- API integration
- Feature engineering
- Git & GitHub
- Data modeling
- Forecasting
- Machine learning

---

## 📡 Data Sources

Marine and weather forecast data are provided by:

Open-Meteo

https://open-meteo.com/

The project uses the Open-Meteo Marine API and Weather Forecast API.

---

## ⚠️ Limitations

The current model has several limitations.

The Surf Score is based on manually defined rules and weights rather than a statistically trained model.

The project also uses initial break-specific parameters for preferred swell and wind directions. These parameters should be validated and refined using additional surf knowledge and historical observations.

The model does not currently incorporate factors such as:

Tide
Local bathymetry
Reef or beach morphology
Wave breaking characteristics
Historical surf observations
Real-time observations
Surf reports from local surfers

Therefore, the Surf Score should be considered an experimental analytical indicator, not a definitive prediction of surf quality.

---

## 🤝 Contributing

Contributions, ideas and feedback are welcome.

If you find an issue, have suggestions for improving the Surf Score, or want to add new surf breaks, feel free to open an issue or submit a pull request.

---

## ⚠️ Disclaimer

Surf conditions can change rapidly and depend on many local factors.

This project is intended for educational, analytical and experimental purposes.

The Surf Score is not a guarantee of surf quality or safety.

Always check current local conditions and use appropriate judgment before entering the water.

---

## 📄 License

This project will be released as an open-source project.
License details will be added as the project develops.