import streamlit as st
import pandas as pd
from engine_util import engine

st.title("📥 Claims Overview")

df = pd.read_sql("SELECT * FROM claims", engine)

st.dataframe(df)
