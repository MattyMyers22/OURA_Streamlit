# Oura Streamlit Dashboard
# @author: Matthew Myers
# 2023-06-17

# Import data from oura_transform
import oura_transform
# Import streamlit
import streamlit as st

# Streamlit dashboard title
st.title("Matthew Myers Oura Ring Data")

# Create sidebar title
st.sidebar.title("Data Category")

# Create sidebar option
data_option = st.sidebar.selectbox("Select Data Options:", ("Heart", "Respiratory", "Sleep", "Activity"))

# Set dashboard header to data selected
st.header(data_option)
