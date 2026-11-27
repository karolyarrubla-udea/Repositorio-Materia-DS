
import streamlit as st
import pandas as pd

st.title("📊 Mis datos")

st.write(
    "Consulta tus resultados y estadísticas "
    "de las partidas realizadas."
)

# Inicializar historial
if "partidas" not in st.session_state:
    st.session_state.partidas = []

partidas = st.session_state.partidas

# Comprobar si existen partidas
if len(partidas) == 0:
    st.info("Todavía no tienes partidas registradas. ¡Ve a Jugar!")
    st.stop()

# Calcular estadísticas
total_partidas = len(partidas)
mejor_puntaje = max(partidas)
promedio = sum(partidas) / total_partidas
puntos_acumulados = sum(partidas)

# Mostrar indicadores
st.subheader("Resumen de actividad")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Partidas jugadas", total_partidas)

with col2:
    st.metric("Mejor puntaje", f"{mejor_puntaje}/5")

with col3:
    st.metric("Puntaje promedio", f"{promedio:.2f}/5")

st.metric("Puntos acumulados", puntos_acumulados)

# Crear tabla de historial
st.subheader("Historial de partidas")

historial = pd.DataFrame({
    "Partida": range(1, total_partidas + 1),
    "Puntaje": partidas
})

st.dataframe(
    historial,
    use_container_width=True,
    hide_index=True
)

# Mostrar progreso
st.subheader("Evolución de puntajes")

st.line_chart(
    historial.set_index("Partida")["Puntaje"]
)

st.caption(
    "Los resultados se conservan durante la sesión "
    "actual de la aplicación."
)
