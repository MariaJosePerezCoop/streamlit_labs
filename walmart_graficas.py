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



fig1=px.bar(df,
                        x='Category',
                        y="Quantity", 
                        orientation="v",
                        title="Cantidad vendida por categoría",
                        labels=dict(Category="Categoría", Quantity="Cantidad"),
                        color_discrete_sequence=["#7ECBB4"],
                        template="presentation")

fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig1)

fig2 = px.pie(df, values='Quantity', names='Ship Mode')
st.plotly_chart(fig2)

fig3 = px.histogram(df, x="State", y='Quantity')
st.plotly_chart(fig3)