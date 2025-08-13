import streamlit as st
import pandas as pd
import os

DATA_FILE = os.path.join("data", "processed_vahan_data.csv")

st.set_page_config(page_title="Vehicle Registration Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE, parse_dates=['date'])

df = load_data()

st.title("🚗 Vehicle Registration Dashboard")

# Filters
categories = st.multiselect("Select Vehicle Category", options=df["vehicle_category"].unique(), default=df["vehicle_category"].unique())
manufacturers = st.multiselect("Select Manufacturer", options=df["manufacturer"].unique(), default=df["manufacturer"].unique())
date_range = st.date_input("Select Date Range", [df["date"].min(), df["date"].max()])

# Apply filters
filtered_df = df[
    (df["vehicle_category"].isin(categories)) &
    (df["manufacturer"].isin(manufacturers)) &
    (df["date"].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))
]

# Display Data
st.dataframe(filtered_df)

# Graphs
st.subheader("Registration Trends")
st.line_chart(filtered_df.groupby("date")["registrations"].sum())

st.subheader("YoY Growth (%)")
st.line_chart(filtered_df.groupby("date")["yoy_growth"].mean())

st.subheader("QoQ Growth (%)")
st.line_chart(filtered_df.groupby("date")["qoq_growth"].mean())
