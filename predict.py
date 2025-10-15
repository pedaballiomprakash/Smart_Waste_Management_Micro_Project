import sqlite3
import pandas as pd

conn = sqlite3.connect("data.db")

df = pd.read_sql_query("SELECT * FROM bin_data", conn)
if df.empty:
    print("No data yet.")
else:
    df["predicted_fill"] = df["fill_level"] * 1.1  # Simple increase
    df["predicted_fill"] = df["predicted_fill"].clip(upper=100)
    print(df[["bin_id", "fill_level", "predicted_fill"]].tail())
