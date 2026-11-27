
import streamlit as st

st.set_page_config(
    page_title="V.P. Agrícola",
    page_icon="🌱",
    layout="wide"
)

paginas = [
    st.Page("pages/inicio.py", title="Inicio", default=True),
    st.Page("pages/explorar.py", title="Explorar"),
    st.Page("pages/jugar.py", title="Jugar"),
    st.Page("pages/mis_datos.py", title="Mis datos")
]

pagina = st.navigation(paginas)

with st.sidebar:
    st.image("assets/logo.jpg", width=150)

pagina.run()
