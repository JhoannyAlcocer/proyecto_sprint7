import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('dataset/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.title('Histograma de distribucion - Odometro vs Cantidad de vehiculos')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


disp_button = st.button('Construir grafico de dispersion') # crear un botón
     
if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.title('Grafico de dispersion - Odometro vs Precio de vehiculos')
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
         
    # crear un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)