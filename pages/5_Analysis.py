import streamlit as st
import pandas as pd
import plotly.express as px
from engine_util import engine

st.title("📈 Analytical Queries")
st.markdown("Select a query to visualize insights based on food listings and claims.")

# Analysis Selector
analysis_options = {
    "Top 10 Cities by Food Listings": """
        SELECT location, COUNT(*) as listing_count
        FROM food_listings
        GROUP BY location
        ORDER BY listing_count DESC
        LIMIT 10;
    """,
    "Top 10 Meal Types": """
        SELECT meal_type, COUNT(*) as total
        FROM food_listings
        GROUP BY meal_type
        ORDER BY total DESC
        LIMIT 10;
    """,
    "Top Providers by Quantity Donated": """
        SELECT p.name AS provider_name, SUM(f.quantity) as total_quantity
        FROM food_listings f
        JOIN providers p ON f.provider_id = p.provider_id
        GROUP BY p.name
        ORDER BY total_quantity DESC
        LIMIT 10;
    """,
    "Most Claimed Food Types": """
        SELECT f.food_type, COUNT(*) as claim_count
        FROM claims c
        JOIN food_listings f ON f.food_id = c.food_id
        GROUP BY f.food_type
        ORDER BY claim_count DESC;
    """
}

selected_analysis = st.selectbox("Choose an analysis", list(analysis_options.keys()))
query = analysis_options[selected_analysis]

df = pd.read_sql(query, engine)

# Chart Display
if df.shape[1] == 2:
    col1, col2 = df.columns
    chart = px.bar(df, x=col1, y=col2, title=selected_analysis)
    st.plotly_chart(chart, use_container_width=True)

# Data Preview
with st.expander("🔍 View Raw Data"):
    st.dataframe(df)
