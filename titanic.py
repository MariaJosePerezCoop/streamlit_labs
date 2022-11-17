import streamlit as st
import numpy as np
import pandas as pd
import datetime

titanic_link='https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'

titanic_data=pd.read_csv(titanic_link)

st.title('titanic app')

sidebar=st.sidebar
sidebar.title('this is the sidebar')
sidebar.write('you can add any element to the sidebar')

today=datetime.date.today()
today_date=sidebar.date_input('Current date:', today)
st.success(f'tu cumple es: {today_date}')

st.header('titanic dataset')

agree=sidebar.checkbox('show dataset overview?')
if agree:
    st.dataframe(titanic_data)

st.header('class description')
selected_class=st.radio('select class', titanic_data['class'].unique())

st.write('selected class:', selected_class)
st.markdown('___')


selected_sex=st.radio('select sex', titanic_data['sex'].unique())
st.write(f'selected option:, {selected_sex}')
st.markdown('___')

optionals=st.beta_expander('Optional Configurations',True)
fare_select=optionals.slider(
'Select the Fare',
min_value=float(titanic_data['fare'].min()),
max_value=float(titanic_data['fare'].max())

)

subset_fare=titanic_data[(titanic_data['fare']>= fare_select)]

st.write(f'Number of records with this fare {fare_select}:{subset_fare.shape[0]}')
st.markdown('___')