import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="E-Commerce Sales Forecast", layout="centered")

# Title and intro
st.title("📊 E-Commerce Sales Forecast")
st.markdown("This app shows future monthly revenue predictions using Facebook Prophet.")
with st.expander("📘 About this Project"):
    st.markdown("""
    This app forecasts monthly sales for a UK-based e-commerce store using 500,000+ transaction records.
    
    **Project steps included:**
    - Data cleaning and monthly aggregation
    - Predictive modeling using Facebook Prophet
    - Confidence interval analysis
    - Dashboard creation using Tableau
    - Streamlit web app deployment for showcasing results

    The forecast shown below is based on time-series modeling of past sales trends.
    """)

# Load forecast data
try:
    df = pd.read_csv("sales_forecast.csv")
    df['ds'] = pd.to_datetime(df['ds'], format="%d-%m-%Y")

except FileNotFoundError:
    st.error("❌ sales_forecast.csv not found. Please make sure it's in the same folder as app.py.")
    st.stop()

# Display top 12 forecast values
st.subheader("📅 Forecast Table")
st.dataframe(
    df[['ds', 'yhat']].tail(12).reset_index(drop=True).rename(
        columns={'ds': 'Month', 'yhat': 'Forecasted Revenue ($)'}
    ),
    use_container_width=True,
    hide_index=True
)

# Plot forecast
st.subheader("📈 Forecast Chart")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['ds'], df['yhat'], label="Forecast", color='blue')
ax.fill_between(df['ds'], df['yhat_lower'], df['yhat_upper'], alpha=0.3, color='skyblue', label="Confidence Interval")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue ($)")
ax.set_title("Monthly Sales Forecast")
ax.legend()

st.pyplot(fig)

st.subheader("📸 Tableau Dashboard Snapshots")

# Sheet 1 – Sales Trend
st.markdown("### 📈 Sheet 1: Monthly Sales Trend")
st.image("dashboard/sheet1_sales_trend.png", caption="Overall monthly revenue trend over time", use_container_width=True)

# Sheet 2 – Top Products by Revenue
st.markdown("### 🛍️ Sheet 2: Top Products by Revenue")
st.image("dashboard/sheet2_top_products.png", caption="Top-selling products based on total revenue", use_container_width=True)

# Sheet 3 – Revenue by Country
st.markdown("### 🌍 Sheet 3: Revenue by Country")
st.image("dashboard/sheet3_country_revenue.png", caption="Revenue distribution across different countries", use_container_width=True)

# Sheet 4 – Forecast with Confidence Band
st.markdown("### 🔮 Sheet 4: Forecast with Confidence Band")
st.image("dashboard/sheet4_forecast_band.png", caption="Prophet forecast with upper/lower confidence bounds", use_container_width=True)


