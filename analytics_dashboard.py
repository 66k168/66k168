import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def show_analytics():
    conn = sqlite3.connect('data_manager.db')
    
    # Load tables
    properties = pd.read_sql_query("SELECT * FROM properties", conn)
    bookings = pd.read_sql_query("SELECT * FROM bookings", conn)
    
    # Total revenue
    total_revenue = bookings['total_amount'].sum() if not bookings.empty else 0
    st.write(f"💰 Total Revenue: {total_revenue} MAD")
    
    # Revenue per property
    if not bookings.empty:
        revenue_per_property = bookings.groupby('property_id')['total_amount'].sum()
        st.write("🏠 Revenue per Property:")
        st.bar_chart(revenue_per_property)
    
    # Occupancy rate
    occupied = bookings['property_id'].nunique() if not bookings.empty else 0
    total = properties.shape[0] if not properties.empty else 0
    occupancy_rate = (occupied / total) * 100 if total > 0 else 0
    st.write(f"📊 Occupancy Rate: {occupancy_rate:.2f}%")
    
    conn.close()
