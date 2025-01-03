
import streamlit as st
import pandas as pd

# Set page title
st.title("일일 선물 동향 데이터")

# Load data
@st.cache_data
def load_data():
    file_path = "일일 선물동향.xlsx"
    return pd.read_excel(file_path)

data = load_data()

# Display data
st.write("### Excel Data")
st.dataframe(data)

# Optionally allow file download
csv = data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download as CSV",
    data=csv,
    file_name="일일_선물동향.csv",
    mime="text/csv"
)
