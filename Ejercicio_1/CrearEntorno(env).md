# Creación y uso de un entorno virtual en Python con Visual Studio Code

Un entorno virtual en Python permite aislar las librerías de un proyecto, evitando conflictos entre versiones y manteniendo un entorno de trabajo organizado.

A continuación se muestra la **secuencia completa de pasos (1 al 9)** para crear, activar y utilizar un entorno virtual (`env`) en Visual Studio Code.

---

## 1. Abrir el proyecto en Visual Studio Code

1. Abrir Visual Studio Code.
2. Ir a **File → Open Folder**.
3. Seleccionar la carpeta del proyecto.

> El entorno virtual debe crearse dentro de la carpeta del proyecto para que VS Code lo detecte correctamente.

---

## 2. Abrir la terminal integrada de Visual Studio Code

1. Presionar `Ctrl + \``
2. O ir a **Terminal → New Terminal**

La terminal integrada se abrirá directamente en la carpeta del proyecto.

---

## 3. Crear el entorno virtual

El entorno virtual se crea utilizando el módulo `venv` que viene incluido con Python.

```python
# python -m venv env
````
---
## 4. Activar el entorno virtual
Para activar el entorno virtual en la terminal de visual studio

