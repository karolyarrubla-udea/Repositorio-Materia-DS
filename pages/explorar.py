
import streamlit as st
import pandas as pd
import plotly.express as px
from src.data import cargar_datos

st.set_page_config(layout="wide")

st.title("🌱 Explorador Agrícola")
st.caption("Consulta y compara la producción agrícola de Colombia. Fuente: Agronet.")

# Cargar datos
df = cargar_datos()

# Filtros
with st.container(border=True):
    st.subheader("Filtros de consulta")

    col1, col2, col3 = st.columns(3)

    with col1:
        anio = st.selectbox(
            "Año",
            ["Todos"] + sorted(df["Año"].unique().tolist(), reverse=True)
        )

    with col2:
        departamentos = st.multiselect(
            "Departamentos",
            sorted(df["Departamento"].dropna().unique())
        )

    with col3:
        productos = st.multiselect(
            "Productos agrícolas",
            sorted(df["Producto"].dropna().unique())
        )

# Aplicar filtros
filtrado = df.copy()

if anio != "Todos":
    filtrado = filtrado[filtrado["Año"] == anio]

if departamentos:
    filtrado = filtrado[filtrado["Departamento"].isin(departamentos)]

if productos:
    filtrado = filtrado[filtrado["Producto"].isin(productos)]

if filtrado.empty:
    st.warning("No se encontraron registros con los filtros seleccionados.")
    st.stop()

# Indicadores
st.subheader("Resumen de producción")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Registros", f"{len(filtrado):,}")

with col2:
    st.metric(
        "Producción total",
        f"{filtrado['Producción'].sum():,.2f}"
    )

with col3:
    st.metric(
        "Área cosechada",
        f"{filtrado['Área Cosechada'].sum():,.2f}"
    )

st.divider()

# Preparar datos para los gráficos
por_departamento = (
    filtrado.groupby("Departamento", as_index=False)["Producción"]
    .sum()
    .nlargest(10, "Producción")
)

por_producto = (
    filtrado.groupby("Producto", as_index=False)["Producción"]
    .sum()
    .nlargest(10, "Producción")
)

# Gráficos
st.subheader("Comparación de producción")

col1, col2 = st.columns(2)

with col1:
    fig_departamento = px.bar(
        por_departamento,
        x="Producción",
        y="Departamento",
        orientation="h",
        title="Top 10 departamentos por producción"
    )

    fig_departamento.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(fig_departamento, use_container_width=True)

with col2:
    fig_producto = px.bar(
        por_producto,
        x="Producción",
        y="Producto",
        orientation="h",
        title="Top 10 productos por producción"
    )

    fig_producto.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(fig_producto, use_container_width=True)

st.divider()

# Tabla de registros
st.subheader("Registros agrícolas")
st.dataframe(
    filtrado,
    use_container_width=True,
    hide_index=True
)

# Detalle individual
with st.expander("Consultar detalle de un registro"):
    indice = st.selectbox(
        "Selecciona un registro",
        filtrado.index.tolist(),
        format_func=lambda i: (
            f"{filtrado.loc[i, 'Departamento']} - "
            f"{filtrado.loc[i, 'Producto']} "
            f"({filtrado.loc[i, 'Año']})"
        )
    )

    registro = filtrado.loc[indice]

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Departamento:** {registro['Departamento']}")
        st.write(f"**Producto:** {registro['Producto']}")
        st.write(f"**Año:** {registro['Año']}")
        st.write(f"**Ciclo:** {registro['Ciclo']}")

    with col2:
        st.write(f"**Producción:** {registro['Producción']:,.2f}")
        st.write(f"**Área sembrada:** {registro['Área Sembrada']:,.2f}")
        st.write(f"**Área cosechada:** {registro['Área Cosechada']:,.2f}")
        st.write(f"**Rendimiento:** {registro['Rendimiento']:,.2f}")
