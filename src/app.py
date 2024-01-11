# Importación de los paquetes
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sacar los datos del CSV
datos_set = pd.read_csv("data/employees2.csv")

# Ponemos el título
st.title('EMPLEATRONIX')
st.write('Todos los datos sobre los empleados en una aplicación.')
st.write(datos_set) # mostramos el dataframe

st.divider()    # es la linea separadora

on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')

# Crear la gráfica de barras horizontales
fig, ax = plt.subplots()
ax.barh(datos_set['full name'],datos_set['salary'])

# Etiquetas y título
ax.set_xlabel('Salario')
ax.set_ylabel('Nombre Completo')
ax.set_title('Gráfica del salario de cada Empleado')

# Mostrar la gráfica en Streamlit
st.pyplot(fig)