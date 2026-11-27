# Manual de usuario

## Visualizador de Productividad Agrícola (V.P. Agrícola)

**Universidad:** Universidad de Antioquia  
**Curso:** Algoritmos y Programación  
**Versión:** 1.0  
**Año:** 2026

## 1. Introducción

V.P. Agrícola es una aplicación web desarrollada con Python y Streamlit que permite consultar información sobre la producción agrícola en Colombia. Utiliza datos obtenidos del portal Agronet y presenta tablas, indicadores, gráficos y un juego de preguntas relacionadas con los productos agrícolas.

La aplicación fue desarrollada con fines académicos por estudiantes de Ingeniería Industrial de la Universidad de Antioquia.

## 2. Requisitos para ejecutar la aplicación

Se necesita:

- Python 3.13 o una versión compatible.
- Las librerías indicadas en `requirements.txt`.
- El código fuente y el archivo `data/datos.csv`.
- Un navegador web.

### Instalación

Abrir una terminal en la carpeta principal del proyecto e instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

### Ejecución

Desde la misma carpeta, ejecutar:

```powershell
python -m streamlit run app.py
```

Abrir en el navegador la dirección:

`http://localhost:8501`

## 3. Navegación

La aplicación cuenta con cuatro páginas, disponibles desde el menú lateral.

### 3.1. Inicio

Presenta el propósito de V.P. Agrícola, información general del conjunto de datos, indicadores sobre los registros disponibles, integrantes del equipo y fuente de información.

### 3.2. Explorar

Permite consultar la información agrícola mediante tres filtros:

1. **Año:** seleccionar un año o consultar todos.
2. **Departamentos:** seleccionar uno o varios departamentos.
3. **Productos agrícolas:** seleccionar uno o varios productos.

Los filtros modifican automáticamente los resultados.

La página también presenta:

- Cantidad de registros encontrados.
- Producción total y área cosechada.
- Gráficos comparativos por departamento y producto.
- Tabla interactiva de registros.
- Detalle de un registro seleccionado.

Cuando una combinación de filtros no produce resultados, la aplicación muestra un mensaje informativo.

### 3.3. Jugar

El juego "¿Qué cultivo produce más?" permite comparar dos productos agrícolas.

**Instrucciones:**

1. Ingresar a la página Jugar.
2. Leer los nombres de los dos productos.
3. Seleccionar el producto que considere de mayor producción total registrada.
4. Consultar la respuesta y los valores de producción.
5. Avanzar a la siguiente pregunta.

Cada partida tiene cinco preguntas. Cada respuesta correcta suma un punto.

Al finalizar, el sistema presenta el puntaje y guarda automáticamente el resultado de la partida. El usuario puede seleccionar "Jugar de nuevo" para iniciar otra partida.

### 3.4. Mis datos

Esta página permite consultar los resultados de las partidas realizadas durante la sesión.

Presenta:

- Número de partidas jugadas.
- Mejor puntaje obtenido.
- Puntaje promedio.
- Puntos acumulados.
- Historial de partidas.
- Gráfico de evolución de puntajes.

Si todavía no existen partidas registradas, se muestra un mensaje invitando al usuario a jugar.

**Importante:** Los resultados se conservan durante la sesión activa de Streamlit. No se almacenan en una base de datos ni en una cuenta personal.

## 4. Recomendaciones de uso

- Utilizar los filtros de Explorar para comparar grupos de registros.
- Revisar el año seleccionado antes de interpretar los resultados.
- Tener presente que los gráficos de producción pueden sumar registros correspondientes a varios años.
- Mantener la aplicación ejecutándose en la terminal mientras se utiliza.

## 5. Fuente de información y licencia

**Fuente de datos:** Agronet, estadísticas agrícolas.

https://agronet.gov.co/estadisticas/agricola

**Licencia del software:** MIT. Consultar `docs/LICENSE.md`.

## 6. Equipo desarrollador

- Dahiana García Herrera.
- Karoly Arrubla Rojas.
- Jose Luis Correa Salazar.

Universidad de Antioquia, 2026.
