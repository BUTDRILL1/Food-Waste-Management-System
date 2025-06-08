import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from engine_util import engine

st.set_page_config(page_title="EDA", layout="wide")
st.title("🧪 Exploratory Data Analysis")

df = pd.read_sql("SELECT * FROM food_listings", engine)

# Filter
st.sidebar.header("🔍 Filter Data")
meal_filter = st.sidebar.multiselect("Meal Type", df["meal_type"].unique(), default=list(df["meal_type"].unique()))
type_filter = st.sidebar.multiselect("Food Type", df["food_type"].unique(), default=list(df["food_type"].unique()))

filtered = df[(df["meal_type"].isin(meal_filter)) & (df["food_type"].isin(type_filter))]

# Row 1
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧃 Food Type Distribution")
    fig1 = px.histogram(filtered, x="food_type", color="meal_type", barmode="group")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("### 🥘 Meal Type Distribution")
    fig2 = px.pie(filtered, names="meal_type", title="Meal Type Share")
    st.plotly_chart(fig2, use_container_width=True)

# Row 2
st.markdown("### 🧮 Quantity Distribution")

fig3 = px.histogram(
    filtered,
    x="quantity",
    nbins=20,
    title="Quantity Distribution",
    labels={"quantity": "Quantity"},
    color_discrete_sequence=["steelblue"]
)

fig3.update_layout(
    bargap=0.1,
    xaxis_title="Quantity",
    yaxis_title="Number of Listings",
    hoverlabel=dict(bgcolor="white", font_size=12)
)

st.plotly_chart(fig3, use_container_width=True)

# Optional
with st.expander("📋 View Raw Data"):
    st.dataframe(filtered)
