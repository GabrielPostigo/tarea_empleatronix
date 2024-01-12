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
bars = ax.barh(datos_set['full name'],datos_set['salary'], color = coloru)

# Etiquetas y título
ax.set_xlabel('Salario')
ax.set_ylabel('Nombre Completo')
# ax.set_title('Gráfica del salario de cada Empleado')

# Ajustar el rango del eje X para que se extienda hasta 4500
ax.set_xlim(right=4500)

if not on:
    ax.set_yticklabels([])

# Mostrar los valores junto a las barras si on2 está activado
if on2:
    for bar in bars:
        width = bar.get_width()
        label_x_pos = width if width >= 0 else width - 5  # Posición de la etiqueta
        ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{int(width)}', ha='left', va='center')


# Mostrar la gráfica en Streamlit
st.pyplot(fig)