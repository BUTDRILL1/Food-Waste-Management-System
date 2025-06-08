import streamlit as st
import pandas as pd
from engine_util import engine

st.title("🍱 Food Listings")

# SQL JOIN to include provider name and contact
query = """
SELECT 
    f.food_id,
    f.food_name,
    f.quantity,
    f.expiry_date,
    f.location,
    f.food_type,
    f.meal_type,
    p.name AS provider_name,
    p.contact AS provider_contact
FROM food_listings f
JOIN providers p ON f.provider_id = p.provider_id
"""
df = pd.read_sql(query, engine)

# Filters 
with st.expander("🔍 Filters", expanded=True):
    location = st.selectbox("Filter by Location", ["All"] + sorted(df["location"].dropna().unique()))
    meal = st.selectbox("Filter by Meal Type", ["All"] + sorted(df["meal_type"].dropna().unique()))
    
    if location != "All":
        df = df[df["location"] == location]
    if meal != "All":
        df = df[df["meal_type"] == meal]

# Data Display
df = df[[
    "food_id", "food_name", "quantity", "expiry_date",
    "meal_type", "food_type", "location",
    "provider_name", "provider_contact"
]]

st.dataframe(df, use_container_width=True)
