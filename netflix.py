import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(page_title="Movie Search",
                page_icon=":movie_camera:",
                layout="wide")

st.title('Netflix App')
st.caption('_Search any movie by title or director_')

DATA_URL='movies.csv'
df=pd.read_csv(DATA_URL)

#SIDEBAR

lista_peliculas=st.sidebar.checkbox('Show all titles')
lista_directores=st.sidebar.checkbox('Show titles by director')

pelicula=st.sidebar.text_input('Type the title of the movie')

directores=df['director']

if st.sidebar.button('Search Movies'):
    resultado_pelicula = df[df['name'].str.upper().str.contains(pelicula.upper())]
    num_pelis=resultado_pelicula.shape[0]
    st.subheader('Search Results')
    st.write('Total movies: ', num_pelis)
    st.dataframe(resultado_pelicula)

resultado_director=st.sidebar.selectbox('Select the director: ', directores)

if st.sidebar.button('By Director'):
    resultado_pelicula = df[df['name'].str.upper().str.contains(pelicula.upper()) & df['director'].str.upper().str.contains(resultado_director.upper())]
    num_pelis=resultado_pelicula.shape[0]
    st.subheader('Search Results')
    st.write('Total movies: ', num_pelis)
    st.dataframe(resultado_pelicula)



#Page

@st.cache
def load_data(directores):
    data=pd.read_csv(DATA_URL)
    director=data[data['director'].str.contains(directores)]
    return director

if (lista_peliculas):
    st.subheader('Movie list')
    num_mov=len(df.axes[0]) 
    st.dataframe(df)
    st.write('Total movies: ', num_mov)
    

if (lista_directores):
    st.subheader("Director's Movie List")
    filtrodirector=load_data(resultado_director)
    num_dir=filtrodirector.shape[0]
    st.dataframe(filtrodirector)  
    st.write('Movies by director: ',num_dir)

