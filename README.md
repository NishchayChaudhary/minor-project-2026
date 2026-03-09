# LimaAir-Forecaster: AI-Driven Air Quality Monitoring

An Air Quality Monitoring and Forecasting System designed for **Lima City**. This project utilizes Machine Learning (Random Forest) to process data from low-cost sensors and forecast $PM_{2.5}$ levels, accounting for Lima's unique coastal micro-climates.


## Project Structure

LimaAir-Forecaster/
│
├── data/                # Dataset files
├── models/              # Trained ML models
├── src/                 # Source code
│   ├── train_model.py
│   ├── predict.py
│
├── README.md
├── requirements.txt


## Features
- **Multi-Parameter Analysis:** Processes $PM_{2.5}$, $PM_{10}$, $NO_2$, $SO_2$, $CO$, and $O_3$.
- **Meteorological Integration:** Factors in Temperature, Humidity, and Wind Speed—critical for Lima's inversion layer.
- **AI Forecasting:** Uses a `RandomForestRegressor` to predict next-hour pollution levels.
- **Manual Input Interface:** Simple CLI for testing and data validation.

## The Science
Lima's air quality is heavily influenced by the **Humboldt Current**, which creates a persistent thermal inversion. This system is designed to identify patterns where high humidity and low wind speed trap pollutants near the surface.



## Tech Stack
- **Language:** Python 3.x
- **Libraries:** - `pandas` (Data manipulation)
  - `scikit-learn` (Machine Learning)
  - `numpy` (Numerical processing)

  ## Future Improvements

- Add real-time sensor data integration
- Deploy model using Flask API
- Build a web dashboard for visualization
- Integrate live weather APIs

## Getting Started

### Prerequisites
Install the required dependencies:
```bash
pip install pandas scikit-learn numpy
