import pandas as pd
import os

DATA_DIR = "data"
RAW_DATA_FILE = os.path.join(DATA_DIR, "raw_vahan_data.csv")
PROCESSED_DATA_FILE = os.path.join(DATA_DIR, "processed_vahan_data.csv")

def calculate_growth(df):
    df = df.copy()
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['quarter'] = pd.DatetimeIndex(df['date']).quarter

    # Year-over-Year growth
    df['yoy_growth'] = df.groupby(['vehicle_category', 'manufacturer'])['registrations'].pct_change(periods=4) * 100

    # Quarter-over-Quarter growth
    df['qoq_growth'] = df.groupby(['vehicle_category', 'manufacturer'])['registrations'].pct_change(periods=1) * 100

    return df

def process_data():
    df = pd.read_csv(RAW_DATA_FILE, parse_dates=['date'])
    processed_df = calculate_growth(df)
    processed_df.to_csv(PROCESSED_DATA_FILE, index=False)
    print(f"Processed data saved to {PROCESSED_DATA_FILE}")

if __name__ == "__main__":
    process_data()
