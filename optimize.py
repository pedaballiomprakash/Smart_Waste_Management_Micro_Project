import sqlite3
import pandas as pd

conn = sqlite3.connect("data.db")
df = pd.read_sql_query("SELECT * FROM bin_data", conn)

if df.empty:
    print("No data found.")
else:
    df = df.sort_values(by="fill_level", ascending=False)
    print("Recommended pickup order:")
    print(df[["bin_id", "fill_level"]].head(5))
