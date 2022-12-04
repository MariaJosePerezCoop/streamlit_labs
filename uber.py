import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title="Uber",
                   page_icon=":car:",layout='wide', initial_sidebar_state='expanded')

st.title('Rutas Uber')

st.write('_Viajes de Uber en la ciudad de Nueva York con filtros por hora_')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data=load_data(100)
st.dataframe(data)

hour_to_filter = st.slider('hour', 0, 23, 15)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.map(filtered_data)
