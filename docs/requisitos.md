
# Especificación de requisitos

## 1. Descripción general

El Visualizador de Productividad Agrícola es una aplicación web desarrollada en Python utilizando Streamlit y Pandas.

Su propósito es permitir que los usuarios consulten, filtren y comparen información sobre la producción agrícola en Colombia mediante tablas, indicadores y gráficos interactivos.

La aplicación también contará con un juego de preguntas relacionadas con los datos agrícolas.

## 2. Requisitos funcionales

Los requisitos funcionales describen las acciones que podrá realizar el usuario dentro de la aplicación.

| Código | Requisito | Descripción |
|--------|-----------|-------------|
| RF01 | Página de inicio | Presentar el nombre, logo, descripción del proyecto, integrantes y al menos tres indicadores generales. |
| RF02 | Carga de datos | Leer la información agrícola desde un archivo CSV mediante Pandas. |
| RF03 | Consulta de datos | Mostrar los registros agrícolas en una tabla interactiva. |
| RF04 | Filtros | Permitir filtrar los datos mediante al menos tres criterios disponibles en el conjunto de datos. |
| RF05 | Detalle de registros | Mostrar información del registro seleccionado por el usuario. |
| RF06 | Indicadores | Calcular al menos tres estadísticas a partir de los datos filtrados. |
| RF07 | Gráficos | Presentar al menos dos gráficos que permitan comparar los datos agrícolas. |
| RF08 | Juego interactivo | Ofrecer preguntas o retos relacionados con los datos agrícolas reales. |
| RF09 | Puntuación | Calcular y mostrar el puntaje obtenido por el usuario en cada partida. |
| RF10 | Historial de partidas | Conservar los resultados de las partidas durante la sesión. |
| RF11 | Reiniciar juego | Permitir iniciar una nueva partida sin perder las estadísticas anteriores de la sesión. |
| RF12 | Mis datos | Mostrar estadísticas, historial y progreso del usuario durante la sesión. |
| RF13 | Navegación | Permitir desplazarse entre Inicio, Explorar, Jugar y Mis datos. |

## 3. Requisitos no funcionales

Los requisitos no funcionales establecen las condiciones generales de funcionamiento de la aplicación.

| Código | Categoría | Requisito |
|--------|-----------|-----------|
| RNF01 | Usabilidad | La aplicación tendrá una interfaz sencilla, con instrucciones claras y navegación intuitiva. |
| RNF02 | Rendimiento | Los filtros y gráficos deberán actualizarse sin demoras excesivas durante el uso normal. |
| RNF03 | Compatibilidad | La aplicación deberá funcionar en navegadores web modernos. |
| RNF04 | Seguridad | No se solicitarán contraseñas ni datos personales para utilizar las funciones principales. |
| RNF05 | Fiabilidad | El programa deberá manejar archivos inexistentes, valores faltantes y consultas sin resultados. |
| RNF06 | Mantenimiento | El código se organizará en funciones y archivos separados para facilitar su comprensión y modificación. |
| RNF07 | Accesibilidad | Los textos, botones y gráficos deberán ser legibles y fáciles de identificar. |
| RNF08 | Disponibilidad | La aplicación podrá ejecutarse localmente con Python y las librerías necesarias instaladas. |
| RNF09 | Consistencia | Las cuatro páginas mantendrán una identidad visual común. |
| RNF10 | Integridad | Los datos originales se conservarán separados de los datos procesados. |

## 4. Herramientas de desarrollo

- **Python:** lenguaje de programación principal.
- **Streamlit:** construcción de la aplicación web.
- **Pandas:** lectura, limpieza y análisis de datos.
- **Plotly Express:** creación de gráficos interactivos.
- **CSV:** almacenamiento de los datos procesados.
- **GitHub:** control de versiones y colaboración entre integrantes.

## 5. Alcance del proyecto

La aplicación permitirá explorar información agrícola a partir de un conjunto de datos público.

El desarrollo se limitará a las funcionalidades establecidas para el curso de Algoritmos y Programación. No se implementarán bases de datos externas, sistemas de autenticación ni conexiones a servicios de terceros.

Los datos utilizados serán preparados previamente y almacenados en un archivo CSV local.

La información sobre productividad agrícola dependerá de las variables y la cobertura del conjunto de datos seleccionado.
