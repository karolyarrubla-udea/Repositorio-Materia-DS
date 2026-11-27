
import streamlit as st
import pandas as pd
from src.data import cargar_datos

st.set_page_config(layout="wide")

st.title("🌱 Visualizador de Productividad Agrícola")

st.write(
    "Aplicación desarrollada para el curso de Algoritmos "
    "y Programación de la Universidad de Antioquia."
)

# Cargar datos
df = cargar_datos()

# Presentación
st.subheader("¿Qué es V.P. Agrícola?")

st.write(
    "Es una aplicación que permite explorar información "
    "sobre la producción agrícola en Colombia mediante "
    "tablas, filtros, gráficos y un juego interactivo."
)

# Información de los datos
st.subheader("Nuestros datos")

st.write(
    "El conjunto de datos contiene información sobre "
    "productos agrícolas, departamentos, años, "
    "áreas sembradas y cosechadas, producción y rendimiento."
)

# Indicadores generales
st.subheader("Indicadores generales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Registros", f"{len(df):,}")

with col2:
    st.metric("Departamentos", df["Departamento"].nunique())

with col3:
    st.metric("Productos agrícolas", df["Producto"].nunique())

# Funcionalidades
st.subheader("¿Qué puedes hacer?")

st.write("""
- **Explorar:** consultar y filtrar datos agrícolas.
- **Jugar:** participar en retos sobre producción agrícola.
- **Mis datos:** consultar resultados y estadísticas de juego.
""")

# Equipo
st.subheader("Equipo desarrollador")

st.write(
    "Dahiana García Herrera, Karoly Arrubla Rojas "
    "y Jose Luis Correa Salazar."
)

# Créditos
st.subheader("Créditos y licencia")

st.write(
    "Desarrollado por estudiantes de Ingeniería Industrial "
    "de la Universidad de Antioquia."
)

st.write("Fuente de datos: Agronet.")
st.write("Licencia del software: MIT.")

st.subheader("Fuente de información")

st.write(
    "Los datos utilizados en esta aplicación fueron obtenidos "
    "del portal Agronet, en su sección de estadísticas agrícolas."
)

st.markdown(
    "[Consultar fuente original]"
    "(https://agronet.gov.co/estadisticas/agricola)"
)
