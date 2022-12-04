import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time
import datetime
from datetime import datetime
import matplotlib.pyplot as plt


st.set_page_config(page_title="Citibike",
                page_icon=":bike:",
                layout="wide")


st.title('Citibike Map')

DATA_URL='citibike-tripdata.csv'

df_rows=st.sidebar.checkbox('Visualizar toda la info')

@st.cache
def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    return data

if (df_rows):
    data_load_state=st.text('Loading...')
    data=load_data(500)
    data_load_state.text('Done.. using @st.cache')
    st.dataframe(data)

df = pd.read_csv('citibike-tripdata.csv')
df = df.rename(columns={"start_lat": "lat", "start_lng": "lon"})

df['started_at']=pd.to_datetime(df['started_at'])

df['hour'] = df['started_at'].dt.strftime('%H')
total_hours=df['hour'].value_counts()
total_hours=pd.DataFrame(total_hours)
total_hours=total_hours.reset_index()
total_hours=total_hours.rename(columns={'index':'hour','hour':'count'})
total_hours=total_hours.sort_values(by='hour')

hour_data=st.sidebar.checkbox('Recorridos por hora')
if (hour_data):
    fig = px.bar(total_hours, x='hour', y='count')
    st.plotly_chart(fig)

df['hour']=df['hour'].astype('int64')


optionals=st.sidebar.expander('Mapa',True)
hour_select=optionals.slider(
    'select the hour',
    min_value=int(df['hour'].min()),
    max_value=int(df['hour'].max()),
)

subset_hour=df[(df['hour'] == hour_select)]
map_data=subset_hour[['lat','lon']]

st.map(map_data)