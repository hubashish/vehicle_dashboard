import pandas as pd
import requests
from datetime import datetime
import os

DATA_DIR = "data"
RAW_DATA_FILE = os.path.join(DATA_DIR, "raw_vahan_data.csv")

def scrape_vahan_data():
    """
    This simulates scraping from Vahan Dashboard.
    Replace this with actual scraping logic if needed.
    """
    # Example simulated dataset
    data = {
        "date": pd.date_range(start="2022-01-01", periods=8, freq="Q"),
        "vehicle_category": ["2W", "3W", "4W", "2W", "3W", "4W", "2W", "4W"],
        "manufacturer": ["Honda", "Bajaj", "Maruti", "Honda", "Bajaj", "Maruti", "Honda", "Maruti"],
        "registrations": [5000, 1200, 3000, 5500, 1500, 3100, 6000, 3300]
    }
    df = pd.DataFrame(data)
    
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(RAW_DATA_FILE, index=False)
    print(f"Raw data saved to {RAW_DATA_FILE}")

if __name__ == "__main__":
    scrape_vahan_data()
