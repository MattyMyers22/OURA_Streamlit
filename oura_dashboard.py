# Oura Streamlit Dashboard
# @author: Matthew Myers
# 2023-06-17

# Import data from oura_transform
import oura_transform
# Import streamlit
import streamlit as st

# Streamlit dashboard title
st.write('Matthew Myers Oura Ring Data')

# Create two columns for charts
col1, col2 = st.columns(2)

# Show past 90 hrv chart in col1
col1.plotly_chart(oura_transform.hrv_past_90, use_container_width=True)
# Show quarterly hrv chart in col2
col2.plotly_chart(oura_transform.hrv_qtr, use_container_width=True)

# Show past 90-day Avg Resting Heart Rate chart
col1.plotly_chart(oura_transform.heart_rate_past_90, use_container_width=True)
# Show quarterly Avg Resting Heart Rate chart
col2.plotly_chart(oura_transform.heart_rate_qtr, use_container_width=True)

# Show past 90-day Avg Respiratory Rate chart
col1.plotly_chart(oura_transform.resp_rate_past_90, use_container_width=True)
# Show quarterly Avg Respiratory Rate chart
col2.plotly_chart(oura_transform.resp_rate_qtr, use_container_width=True)

# Show past 90-day Sleep Efficiency chart
col1.plotly_chart(oura_transform.sleep_effic_past_90, use_container_width=True)
# Show quarterly Sleep Efficiency chart
col2.plotly_chart(oura_transform.sleep_effic_qtr, use_container_width=True)

# Show past 90-day Steps chart
col1.plotly_chart(oura_transform.steps_past_90, use_container_width=True)
# Show quarterly Steps chart
col2.plotly_chart(oura_transform.steps_qtr, use_container_width=True)
