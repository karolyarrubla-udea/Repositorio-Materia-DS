
import streamlit as st
import pandas as pd

st.title("Explorar datos agrícolas")
st.write("Consulta y compara la producción agrícola en Colombia.")

# Cargar datos
df = pd.read_csv("data/datos.csv")

# Filtros
st.subheader("Filtros")

col1, col2, col3 = st.columns(3)

with col1:
    anio = st.selectbox("Año", ["Todos"] + sorted(df["Año"].unique().tolist(), reverse=True))

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

# Validar resultados
if filtrado.empty:
    st.warning("No se encontraron registros con los filtros seleccionados.")
    st.stop()

# Indicadores
st.subheader("Indicadores generales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Registros", f"{len(filtrado):,}")

with col2:
    st.metric("Producción total", f"{filtrado['Producción'].sum():,.2f}")

with col3:
    st.metric("Área cosechada", f"{filtrado['Área Cosechada'].sum():,.2f}")

# Gráficos
st.subheader("Visualización de datos")

col1, col2 = st.columns(2)

with col1:
    st.write("**Producción por departamento**")

    produccion_departamento = (
        filtrado.groupby("Departamento")["Producción"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(produccion_departamento)

with col2:
    st.write("**Producción por producto**")

    produccion_producto = (
        filtrado.groupby("Producto")["Producción"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.bar_chart(produccion_producto)

# Tabla interactiva
st.subheader("Registros agrícolas")
st.dataframe(filtrado, use_container_width=True, hide_index=True)

# Detalle de un registro
st.subheader("Detalle del registro")

indice = st.selectbox(
    "Selecciona un registro para consultar",
    filtrado.index.tolist(),
    format_func=lambda i: (
        f"{filtrado.loc[i, 'Departamento']} - "
        f"{filtrado.loc[i, 'Producto']} ({filtrado.loc[i, 'Año']})"
    )
)

registro = filtrado.loc[indice]

st.write(f"**Año:** {registro['Año']}")
st.write(f"**Departamento:** {registro['Departamento']}")
st.write(f"**Producto:** {registro['Producto']}")
st.write(f"**Ciclo:** {registro['Ciclo']}")
st.write(f"**Producción:** {registro['Producción']:,.2f}")
st.write(f"**Área sembrada:** {registro['Área Sembrada']:,.2f}")
st.write(f"**Área cosechada:** {registro['Área Cosechada']:,.2f}")
st.write(f"**Rendimiento:** {registro['Rendimiento']:,.2f}")
