# Oura Data Transformation
# @author: Matthew Myers
# 2023-07-08

# Import oura_connection script
import oura_API_extract
# Import plotly for visualizations
import plotly.express as px
# Import pandas for data manipulation
import pandas as pd
# Import datetime and timedelta
from datetime import datetime, timedelta

# Save root url for requests
root_url = 'https://api.ouraring.com/v2/usercollection/'
# unused_data_sets = ['daily_readiness', 'session', 'tag', 'workout', 'heartrate', 'daily_sleep']
# List names for data sets in API requests
data_sets = ['daily_activity', 'sleep']

# Initialize API link dictionary
api_links = {}
# Loop through list of data_set names to add name and link pairs into api_link
for name in data_sets:
    api_links[name] = root_url + name

# Initialize data dictionary
data_dict = {}
# Loop through dictionary to pull data and save as dfs with names
for dataset_name, link in api_links.items():
    # Call and save dataframe with oura_connection
    data = oura_API_extract.call_oura_api(link)
    # Add data to data_dict
    data_dict[dataset_name] = data

# Daily activity columns of interest
activity_columns = ['day', 'steps', 'sedentary_time']
# Create dataframe with activity data of interest
activity_data = data_dict['daily_activity'][activity_columns]
# Set day column to datatime
activity_data['day'] = pd.to_datetime(activity_data['day'])
# Set day column to dt day
activity_data['day'] = activity_data['day'].dt.date

# Sleep data columns of interest
sleep_columns = ['day', 'average_breath', 'average_heart_rate', 'average_hrv', 'efficiency', 'type',
                 'total_sleep_duration', 'id']
# Get sleep data olumns of interest
sleep_data = data_dict['sleep'][sleep_columns]
# Filter sleep data for 'long_sleep' type
sleep_data = sleep_data[sleep_data['type'] == 'long_sleep']

# Get value counts for days
multi_sleep_days = sleep_data['day'].value_counts()
# Filter for days with multiple long sleeps
multi_sleep_days = multi_sleep_days[multi_sleep_days > 1]
# Turn row names for multi_sleep_days into a column
multi_sleep_days = pd.DataFrame(multi_sleep_days)
# Reset index for multi_sleep_days
multi_sleep_days = multi_sleep_days.reset_index()

# Join multi sleep days with sleep data to get just days with multi long sleep sessions
multi_sleep_days = sleep_data.merge(multi_sleep_days, on='day', how='inner')
# Sort by day and then total_sleep_duration descending
multi_sleep_days = multi_sleep_days.sort_values(by=['day', 'total_sleep_duration'], ascending=[True, False])
# Rank total_sleep_duration descending by day
multi_sleep_days['duration_rank'] = (
    multi_sleep_days
    .groupby('day')['total_sleep_duration']
    .rank(ascending=False)
    .astype(int)
)
# Filter multi_sleep_days to not have any ranks of 1
multi_sleep_days = multi_sleep_days[multi_sleep_days['duration_rank'] != 1]
# Filter sleep data for ids not in multi_sleep_days
sleep_data = sleep_data[~sleep_data['id'].isin(multi_sleep_days['id'])]

# May need to have the chunk of code below analyzed for more efficient manipulation

# Convert day column to datetime object
sleep_data['day'] = pd.to_datetime(sleep_data['day'])
# Create column in sleep_data for quarter
sleep_data['quarter'] = sleep_data['day'].dt.quarter.map({1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'})
# Create column in sleep_data for year
sleep_data['year'] = sleep_data['day'].dt.year
# Create a column that concatenates quarter with year
sleep_data['qtr_year'] = (sleep_data['quarter'] + ' ' + sleep_data['year'].astype('str')).astype('category')
# Convert day column to timestamp object with YYYY-MM-DD format
sleep_data['day'] = sleep_data['day'].dt.date

# Get past 90 days of sleep_data
sleep_past_90 = sleep_data[sleep_data['day'] > sleep_data['day'].max() - timedelta(days=90)]
# Get past 90 days of activity_data
activity_past_90 = activity_data[activity_data['day'] > activity_data['day'].max() - timedelta(days=90)]

# Create plot for quarterly HRV data
# Create plot for last 90 days of HRV data
hrv_past_90 = px.line(sleep_past_90, x='day', y='average_hrv', title='Past 90 Days Average HRV')
# Add horizontal line to graph representing average hrv for past 90 days
hrv_past_90.add_hline(
    y=sleep_past_90['average_hrv'].mean(),
    line_dash='dot',
    line_color='black'
)
# Create plot for quarterly Resting Heart Rate data
# Create plot for last 90 days of Resting Heart Rate data
# Create plot for all time steps
# Create plot for last 90 days of steps

print("run ended")
