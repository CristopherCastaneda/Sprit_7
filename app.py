import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
        # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        
        # crear un histogram
        fig = px.histogram(car_data, x="odometer")
     
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
        
dist_button= st.button('Construir una Grafica de Dispersion')# crea un boton
if dist_button: # al hacer clic en el boton
    #escribir el mensaje de salida
    st.write('Creacion de una grafica de dispersion para el conjunto de datos de ventas de coches')
    #crear el grafico
    fig=px.scatter(car_data, x="odometer", y="price")
    #Muestra el grafico
    st.plotly_chart(fig,use_container_width=True)        

