import pandas as pd
import streamlit as st

st.set_page_config(page_title="🏠 Airbnb Data Manager", layout="wide")
st.title("🏠 Airbnb Data Manager")

st.write("Upload your raw Airbnb data file (CSV or Excel) to clean and analyze it instantly.")

# --- File upload ---
uploaded_file = st.file_uploader("📁 Upload Airbnb data", type=["csv", "xlsx"])

if uploaded_file:
    # --- Read file ---
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        st.stop()

    st.subheader("🔹 Raw Data Preview")
    st.dataframe(df.head())

    # --- Basic cleaning ---
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.drop_duplicates().fillna(0)

    # --- Key insights ---
    st.subheader("📊 Dashboard Insights")
    if "price" in df.columns and "reviews" in df.columns:
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Listings", len(df))
        col2.metric("Average Price", f"${df['price'].mean():.2f}")
        col3.metric("Total Reviews", int(df["reviews"].sum()))
    
    if uploaded_file:
    # ... your existing code to read & clean df ...
    # --- Top Listings Insights (add this here) ---
     st.subheader("⭐ Top Listings")
     metric = st.selectbox("Select metric", ["price", "reviews"], key="metric_select_1")
     top_n = st.slider("Number of top listings", 1, 10, 5)
    top_listings = df.sort_values(by=metric, ascending=False).head(top_n)
    st.table(top_listings[["name", "price", "room_type", "reviews"]])

    # --- Filters ---
    st.sidebar.header("🔍 Filters")
    if "room_type" in df.columns:
        room_types = ["All"] + sorted(df["room_type"].unique().tolist())
        selected_room = st.sidebar.selectbox("Room Type", room_types)
        if selected_room != "All":
            df = df[df["room_type"] == selected_room]

    if "price" in df.columns:
        max_price = int(df["price"].max())
        price_limit = st.sidebar.slider("Max Price", 0, max_price, max_price, key="price_slider")
        df = df[df["price"] <= price_limit]

    # --- Top Listings Insights (inside this block!) ---
    st.subheader("⭐ Top Listings")
    metric = st.selectbox("Select metric", ["price", "reviews"])
    top_n = st.slider("Number of top listings", 1, 10, 5, key="top_n_slider")
    top_listings = df.sort_values(by=metric, ascending=False).head(top_n)
    st.table(top_listings[["name", "price", "room_type", "reviews"]])

    # --- Final view ---
    st.subheader("🧹 Cleaned & Filtered Data")
    st.dataframe(df, use_container_width=True)




