# Oura Streamlit Dashboard
# @author: Matthew Myers
# 2023-06-17

# Import data from oura_transform
import oura_transform
# Import streamlit
import streamlit as st

# Streamlit dashboard title
st.write('Matthew Myers Oura Ring Data')

# Create sidebar option
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Heart Rate Variablity', 'Resting Heart Rate', 'Respiratory Rate', 'Sleep',
                                        'Activity'])

# Generate tab1 for HRV
with tab1:
    col1, col2 = st.columns(2)
    col1.plotly_chart(oura_transform.hrv_past_90, use_container_width=True)
    col2.plotly_chart(oura_transform.hrv_qtr, use_container_width=True)

# Generate tab2 for Resting Heart Rate

# Generate tab3 for Respiratory Rate

# Generate tab4 for Sleep

# Generate tab5 for Activity

print('Run Ended')
