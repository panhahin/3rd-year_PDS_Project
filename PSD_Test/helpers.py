"""Reusable data-cleaning helpers."""
import pandas as pd

def clean_data(df):
    """Drop rows with missing values, tidy names."""
    df = df.dropna()
    df.columns = [c.strip().lower() for c in df.columns]
    return df

def average_gpa(df):
    return round(df["gpa"].mean(), 2)