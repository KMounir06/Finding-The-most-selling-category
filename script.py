import pandas as pd
import numpy as np
df = pd.read_csv("retail_store_sales.csv")

df["Item"] = df["Item"].fillna("Unknown")
df["Item"] = df["Item"].replace("Unknown", "Not Specified")
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Price Per Unit"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Quantity"] = df["Quantity"].round().astype(int)
df["Total Spent"] = df["Total Spent"].fillna(df["Total Spent"].mean())
df["Discount Applied"] = df["Discount Applied"].fillna("Unknown")
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"], errors="coerce")
df["Transaction Date"] = df["Transaction Date"].fillna("Unknown")


df["Expected_Total"] = df["Price Per Unit"] * df["Quantity"]
df["Discount Applied"] = df["Total Spent"] < df["Expected_Total"]

df = df.drop(columns="Unamed = 8")


print(df.head())
print(df.tail())
print(df.info())
print(df.dtypes)
print(df.isnull().sum())
print((df == "ERROR").any())
print(df.describe())
print(df.duplicated().sum())
print(df.drop(columns="Expected_Total"))


print(df["Item"].value_counts().to_string())

df.to_csv("Retail_Store.csv" , index = False)
