# Plan de versionado

## Visualizador de Productividad Agrícola

**Universidad:** Universidad de Antioquia  
**Curso:** Algoritmos y Programación  
**Año:** 2026

## 1. Objetivo

Establecer un procedimiento sencillo para registrar y controlar los cambios realizados durante el desarrollo de V.P. Agrícola, utilizando Git y GitHub.

El control de versiones permite conservar el historial del proyecto, identificar modificaciones y facilitar el trabajo colaborativo.

## 2. Repositorio

**Plataforma:** GitHub

**Repositorio:** https://github.com/karolyarrubla-udea/Repositorio-Materia-DS

### Organización de ramas

- `main`: rama principal donde se integran las versiones revisadas.
- `jose-dev`: rama de desarrollo utilizada para implementar y probar cambios antes de incorporarlos a `main`.

El trabajo desarrollado por otros integrantes puede incorporarse mediante sus propias ramas o los mecanismos de colaboración establecidos por el equipo.

## 3. Etapas del desarrollo

| Versión | Etapa | Cambios principales |
|---|---|---|
| 0.1 | Configuración inicial | Creación del repositorio y estructura básica del proyecto. |
| 0.2 | Documentación | Incorporación del README, actas, cronograma, presupuesto, requisitos y licencia MIT. |
| 0.3 | Preparación de datos | Incorporación del conjunto de datos de Agronet, limpieza y exportación del archivo procesado. |
| 0.4 | Primera aplicación funcional | Desarrollo inicial de Streamlit y de la página Explorar. |
| 0.5 | Páginas principales | Implementación de Inicio, Jugar y Mis datos. |
| 0.6 | Mejoras funcionales | Registro automático de partidas y centralización de la lectura de datos. |
| 0.7 | Interfaz y navegación | Incorporación del tema claro, logo, diseño amplio y navegación entre las páginas. |
| 1.0 | Versión final prevista | Pruebas, documentación definitiva e integración de los cambios aprobados en `main`. |

Los números de versión anteriores identifican etapas del desarrollo para fines académicos. No representan etiquetas o publicaciones de GitHub creadas previamente.

## 4. Procedimiento de control de versiones

Antes de comenzar a trabajar, se verificará la rama activa y se consultarán los cambios disponibles en el repositorio.

Para guardar una modificación se utilizarán los siguientes comandos:

**Consultar el estado del repositorio:**

`git status`

**Preparar los archivos modificados:**

`git add nombre_archivo`

**Registrar un cambio:**

`git commit -m "Descripción del cambio"`

**Publicar los cambios:**

`git push origin jose-dev`

Una vez revisados y probados, los cambios podrán integrarse en la rama `main`.

## 5. Convención de mensajes

Se utilizarán descripciones breves para identificar el propósito de los cambios.

| Prefijo | Uso | Ejemplo |
|---|---|---|
| `feat` | Nueva funcionalidad | `feat: Agregar juego agricola` |
| `fix` | Corrección de un problema | `fix: Guardar resultados automaticamente` |
| `style` | Cambios visuales | `style: Configurar tema claro` |
| `docs` | Documentación | `docs: Actualizar manual de usuario` |
| `refactor` | Reorganización del código | `refactor: Centralizar carga de datos` |

## 6. Verificación de cambios

Antes de integrar una versión en la rama principal, se comprobará que:

- La aplicación pueda ejecutarse con Streamlit.
- Las cuatro páginas sean accesibles.
- Los filtros y gráficos respondan correctamente.
- El juego calcule y almacene los puntajes.
- La página Mis datos presente los resultados registrados.
- Los archivos obligatorios estén incluidos en el repositorio.
- No se incorporen entornos virtuales ni archivos temporales.

## 7. Historial y seguimiento

GitHub conserva el historial de confirmaciones (commits), con información sobre los archivos modificados y los cambios realizados.

El equipo utilizará este historial como evidencia del avance del proyecto. Las fechas y los identificadores reales de cada modificación podrán consultarse directamente en el repositorio.

La versión final será la integrada en `main` después de las pruebas y la revisión del equipo.
