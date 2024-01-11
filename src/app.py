# Importación de los paquetes
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sacar los datos del CSV
datos_set = pd.read_csv("employees2.csv")

# Ponemos el título
st.title('EMPLEATRONIX')
st.write('Todos los datos sobre los empleados en una aplicación.')
st.write(datos_set) # mostramos el dataframe

st.divider()    # es la linea separadora