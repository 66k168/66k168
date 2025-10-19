import streamlit as st
from user_access import login, add_sample_employee
from property_manager import get_properties, add_property
from owner_manager import get_owners, add_owner
from booking_manager import get_bookings, add_booking
from analytics_dashboard import show_analytics
from alerts import show_alerts
import pandas as pd
import sqlite3

# Add default admin once
add_sample_employee()

st.title("🏠 Agadir Rentals Data Manager")

# ===== CSV Upload Section =====
st.header("Upload CSV file (Owners)")
uploaded_file = st.file_uploader("Upload Owners CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("✅ CSV loaded successfully!")
    st.dataframe(df)

    # Save to SQLite DB so get_owners() works
    conn = sqlite3.connect('data_manager.db')
    df.to_sql('owners', conn, if_exists='replace', index=False)
    conn.close()
    st.success("✅ Owners data saved to SQLite DB")

# ------------------ Login ------------------
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = login(email, password)
    if user:
        st.success(f"Welcome {user[1]} ({user[3]})")
        menu = ["Owners", "Properties", "Bookings", "Analytics", "Alerts"]
        choice = st.selectbox("Menu", menu)

        if choice == "Owners":
            st.dataframe(get_owners())
        elif choice == "Properties":
            st.dataframe(get_properties())
        elif choice == "Bookings":
            st.dataframe(get_bookings())
        elif choice == "Analytics":
            show_analytics()
        elif choice == "Alerts":
            show_alerts()
    else:
        st.error("❌ Invalid email or password")
