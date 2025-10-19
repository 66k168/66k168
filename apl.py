import streamlit as st
from user_access import login, add_sample_employee
from property_manager import get_properties, add_property
from owner_manager import get_owners, add_owner
from booking_manager import get_bookings, add_booking
from analytics_dashboard import show_analytics
from alerts import show_alerts

# Add default admin once
add_sample_employee()

st.title("🏠 Agadir Rentals Data Manager")

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
