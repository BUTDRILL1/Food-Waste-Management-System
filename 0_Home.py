import streamlit as st

st.set_page_config(
    page_title="Food Waste Management",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🍽️ Food Waste Management System")

st.markdown("""
Welcome to the Local Food Waste Management App.

Use the navigation sidebar on the left to:
- View dashboard insights  
- Browse or filter food listings  
- Add providers, food items, or receivers  
- Manage food claims  
- Analyze trends and patterns  
- Explore EDA visualizations

---
""")
# import pandas as pd
# from engine_util import engine

# df = pd.read_sql("SELECT current_database();", engine)
# st.write("📌 App is connected to database:", df.iloc[0, 0])

# df = pd.read_sql("SELECT * FROM providers ORDER BY provider_id DESC LIMIT 5;", engine)
# st.dataframe(df)
# dt = pd.read_sql("SELECT * FROM receivers ORDER BY receiver_id DESC LIMIT 5;", engine)
# st.dataframe(dt)