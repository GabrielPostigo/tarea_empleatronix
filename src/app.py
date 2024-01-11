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

col1, col2, col3 = st.columns(3)    #creamos las columnas

with col1:
    coloru = st.color_picker('Pick A Color', '#3475B3')

with col2:
    on = st.toggle('Mostrar el nombre')

with col3:
    on2 = st.toggle('Mostrar Sueldo en la barra')
# Crear la gráfica de barras horizontales
fig, ax = plt.subplots()
ax.barh(datos_set['full name'],datos_set['salary'])

# Etiquetas y título
ax.set_xlabel('Salario')
ax.set_ylabel('Nombre Completo')
ax.set_title('Gráfica del salario de cada Empleado')

# Mostrar la gráfica en Streamlit
st.pyplot(fig)