import streamlit as st
import pandas as pd
import plotly.express as px
from engine_util import engine

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("📊 Dashboard")
st.markdown("Quick overview of platform performance and trends.")

providers_df = pd.read_sql("SELECT * FROM providers", engine)
receivers_df = pd.read_sql("SELECT * FROM receivers", engine)
listings_df = pd.read_sql("SELECT * FROM food_listings", engine)
claims_df = pd.read_sql("SELECT * FROM claims", engine)

# Basic Data Overview
with st.container():
    st.subheader("📌 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🧍 Food Providers", len(providers_df))
    col2.metric("🎯 Food Receivers", len(receivers_df))
    col3.metric("🍱 Food Listings", len(listings_df))
    col4.metric("📥 Food Claims", len(claims_df))

st.markdown("---")

# Distribution Charts
col5, col6 = st.columns(2)

with col5:
    st.markdown("### 🥘 Meal Type Distribution")
    if "meal_type" in listings_df.columns:
        fig_meal = px.pie(listings_df, names="meal_type", title="Meal Type Breakdown")
        st.plotly_chart(fig_meal, use_container_width=True)

with col6:
    st.markdown("### 🧃 Food Type Distribution")
    if "food_type" in listings_df.columns:
        fig_food = px.pie(listings_df, names="food_type", title="Food Type Breakdown")
        st.plotly_chart(fig_food, use_container_width=True)

st.markdown("---")

# Trend Chart
st.subheader("📈 Monthly Claim Volume")
claims_df["timestamp"] = pd.to_datetime(claims_df["timestamp"])
claims_df["month"] = claims_df["timestamp"].dt.to_period("M").astype(str)

monthly_trend = claims_df.groupby("month").size().reset_index(name="claim_count")
fig_trend = px.bar(monthly_trend, x="month", y="claim_count", title="Claims Over Time")
st.plotly_chart(fig_trend, use_container_width=True)
