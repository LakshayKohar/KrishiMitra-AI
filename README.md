# KrishiMitra AI

KrishiMitra AI is an AI-powered agricultural decision support platform using satellite imagery, weather data, and machine learning.

## Features

- Google Earth Engine integration
- Sentinel-2 satellite imagery
- NDVI, NDWI, MSI calculation
- Cloud masking
- Crop health monitoring
- Moisture stress detection
- Weather intelligence
- Irrigation advisory
- Crop classification framework
- Growth stage detection
- Time-series dataset builder
- Interactive Streamlit dashboard
- PDF and JSON report export

## Tech Stack

- Python
- Streamlit
- Google Earth Engine
- Sentinel-2
- Folium
- Open-Meteo API
- Scikit-learn
- Pandas

## Run Locally

```bash
git clone <repo-url>
cd KrishiMitra-AI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m streamlit run src/dashboard/app.py
```
