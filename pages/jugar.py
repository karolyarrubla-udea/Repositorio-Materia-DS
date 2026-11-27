
import random
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.title("🌱 ¿Qué cultivo produce más?")
st.write("Pon a prueba tus conocimientos sobre la producción agrícola en Colombia.")

# Cargar los datos
df = pd.read_csv("data/datos.csv")

# Calcular la producción total por producto
produccion = df.groupby("Producto")["Producción"].sum()

# Preparar las variables del juego
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0

if "pregunta" not in st.session_state:
    st.session_state.pregunta = 1

if "opciones" not in st.session_state:
    st.session_state.opciones = []

if "respuesta" not in st.session_state:
    st.session_state.respuesta = None

if "partidas" not in st.session_state:
    st.session_state.partidas = []

# Función para generar una pregunta
def nueva_pregunta():
    productos = produccion.index.tolist()
    st.session_state.opciones = random.sample(productos, 2)
    st.session_state.respuesta = None


# Función para comprobar la respuesta
def responder(producto):
    opcion1, opcion2 = st.session_state.opciones

    if produccion[opcion1] >= produccion[opcion2]:
        correcto = opcion1
    else:
        correcto = opcion2

    if producto == correcto:
        st.session_state.puntaje += 1
        st.session_state.respuesta = "¡Correcto! 🎉"
    else:
        st.session_state.respuesta = f"Incorrecto. La respuesta era {correcto}."


# Iniciar el juego
if not st.session_state.opciones:
    nueva_pregunta()

st.divider()

# Mostrar la pregunta
st.subheader(f"Pregunta {st.session_state.pregunta} de 5")
st.metric("Puntaje actual", st.session_state.puntaje)

opcion1, opcion2 = st.session_state.opciones

st.write("**¿Cuál de estos productos tiene mayor producción total registrada?**")

col1, col2 = st.columns(2)

with col1:
    if st.button(opcion1, use_container_width=True,
                 disabled=st.session_state.respuesta is not None):
        responder(opcion1)
        st.rerun()

with col2:
    if st.button(opcion2, use_container_width=True,
                 disabled=st.session_state.respuesta is not None):
        responder(opcion2)
        st.rerun()

# Mostrar resultado
if st.session_state.respuesta is not None:

    st.info(st.session_state.respuesta)

    st.write(f"{opcion1}: {produccion[opcion1]:,.2f}")
    st.write(f"{opcion2}: {produccion[opcion2]:,.2f}")

    if st.session_state.pregunta < 5:

        if st.button("Siguiente pregunta"):
            st.session_state.pregunta += 1
            nueva_pregunta()
            st.rerun()

    else:
        # Guardar el resultado una sola vez
        if "partida_guardada" not in st.session_state:
            st.session_state.partida_guardada = False

        if not st.session_state.partida_guardada:
            st.session_state.partidas.append(st.session_state.puntaje)
            st.session_state.partida_guardada = True

        st.success(f"¡Partida terminada! Puntaje: {st.session_state.puntaje}/5")

        if st.button("Jugar de nuevo"):
            st.session_state.puntaje = 0
            st.session_state.pregunta = 1
            st.session_state.partida_guardada = False
            nueva_pregunta()
            st.rerun()
