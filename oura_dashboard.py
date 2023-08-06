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
data_option = st.sidebar.selectbox("Select Data Options:", ("Heart", "Sleep", "Activity"))

# If heart selector
# 2x2 columns and rows for heart charts
# Else if sleep selector
# 2x2 columns and rows for sleep charts
# Else
# 2 columns for activity charts
# List any potential data of interest?

# Set dashboard header to data selected
st.header(data_option)
