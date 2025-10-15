import streamlit as st
import sqlite3
import pandas as pd

st.title("Smart Waste Management Dashboard")

conn = sqlite3.connect("data.db")
df = pd.read_sql_query("SELECT * FROM bin_data ORDER BY timestamp DESC LIMIT 20", conn)

if df.empty:
    st.warning("No bin data yet. Run simulator.py and ingest_sqlite.py first.")
else:
    st.subheader("Latest Bin Data")
    st.dataframe(df)
    st.bar_chart(df["fill_level"])
