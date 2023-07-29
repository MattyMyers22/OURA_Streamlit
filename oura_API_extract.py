# Oura API Connection
# @author: Matthew Myers
# 2023-05-20

# Import requests package
import requests
# Import datetime package
from datetime import datetime, timedelta
# Import pandas package
import pandas as pd
# Import config file for API key
from config import oura_api_key

# Set end date to yesterday
yesterday = datetime.now().date() - timedelta(days=1)


def call_oura_api(url, start_date='2020-01-01', end_date=yesterday):
    """
    Calls Oura API V2 and returns data as a dataframe
    :param url: url of interest as a string
    :param start_date: start date of interest as a string
    :param end_date: end date of interest as a string
    :return: df, a dataframe of the data extracted
    """

    # Set start date for data pull
    start_date = start_date
    # Set end date for data pull
    end_date = end_date
    # Set url for api request
    url = url
    # Set parameters for API request
    params = {
        'start_date': start_date,
        'end_date': end_date
    }
    # Set headers / authorization key
    headers = {
      'Authorization': oura_api_key
    }

    # Initial API data request
    response = requests.request('GET', url, headers=headers, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        # Create a list with json data
        data = response.json()['data']
        # Set next_token value in params
        params['next_token'] = response.json()['next_token']
        # Loop API pull while next_token is not None
        while params['next_token'] is not None:
            # Make another API request
            response = requests.request('GET', url, headers=headers, params=params)

            # Check if the response was successful
            if response.status_code == 200:
                # Create a list with json data
                data.extend(response.json()['data'])
                # Set next_token value in params
                params['next_token'] = response.json()['next_token']
            else:
                raise Exception("Error getting data from Oura ring API V2: " + str(response.status_code))

        # Create dataframe from data
        df = pd.json_normalize(data)

        # Return data
        return df
