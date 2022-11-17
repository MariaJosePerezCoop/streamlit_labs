import streamlit as st
import numpy as np
import pandas as pd

st.title('streamlit con sidebar')
sidebar=st.sidebar
sidebar.title('título de barra lateral')

sidebar.write('Informacion del sidebar')

if sidebar.checkbox('Show dataframe'):
    chart_data=pd.DataFrame(
        np.random.randint(1,10,size=(20,3)),
        columns=['a','b','c'])

    st.dataframe(chart_data)
