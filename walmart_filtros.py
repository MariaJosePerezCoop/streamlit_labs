import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Walmart",
                   page_icon=":shopping_trolley:",layout='wide', initial_sidebar_state='expanded')

st.title('Walmart USA')
st.subheader(':bar_chart: Interactive Dashboard')

st.write('_Utiliza filtros de información para visualizar hallazgos_')


DATA_URL='https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'

@st.cache
def load_data(DATA_URL):
    df=pd.read_csv(DATA_URL)
    return df

df=load_data(DATA_URL)

st.sidebar.caption('Filtros disponibles')

ship=st.sidebar.radio('Selecciona el modo de envío',df['Ship Mode'].unique())

category=st.sidebar.selectbox('Selecciona la categoría',df['Category'].unique())

discount=st.sidebar.slider('Selecciona el descuento aplicado',
min_value=float(df['Discount'].min()),
max_value=float(df['Discount'].max()))
