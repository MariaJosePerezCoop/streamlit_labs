import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
np.random.randn(100, 2) / [50, 50] + [25.67507, -100.31847],
columns=['lat', 'lon'])

st.dataframe(map_data)
st.map(map_data)

