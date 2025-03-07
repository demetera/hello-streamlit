import streamlit as st
import pandas as pd
import requests
import json

data = requests.get('https://maps.nextbike.net/maps/nextbike-live.json?city=699&domains=bh&list_cities=0&bikes=0')
data_json = json.loads(data.text)
data_city = data_json['countries'][0]['cities'][0]['places']

st.title('Budapest MOL bubi bikes app')

st.write(f'Total stations = {len(data_city)}')
st.write('Sorted by available bikes')
# st.write(data_city[0])

bike_df = pd.DataFrame(columns=['Name', 'Bikes'])

for item in data_city:
    bike_df.loc[len(bike_df)] = [item['name'], item['bikes_available_to_rent']]

bike_df.sort_values(by=['Bikes'], inplace=True, ascending=False)

st.dataframe(bike_df, hide_index=True)
