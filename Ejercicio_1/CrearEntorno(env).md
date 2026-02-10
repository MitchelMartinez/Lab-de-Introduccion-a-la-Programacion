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
python -m venv env
```
---
## 4. Activar el entorno virtual
Para activar el entorno virtual en la terminal de visual studio usar el siguiente comando
```python
env\Scripts\activate
```
### En caso de que de error por permisos deshabilitados
Usar el sigueinte comando una sola vez en la misma terminal
```python
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Cuando el entorno se activa correctamente, la terminal mostrará lo siguiente:
`(env)`

---
## 5. Seleccionar el intérprete de Python en Visual Studio Code

Para asegurarse de que VS Code use el Python del entorno virtual:

Presionar `Ctrl + Shift + P`

Escribir Python: Select Interpreter

Seleccionar el intérprete que incluya `(env)`

Esto garantiza que el editor use el entorno virtual para ejecutar el código.

---
# Instalar una librería dentro del entorno virtual
Con el entorno virtual activo, se pueden instalar librerías usando `pip`
Ejemplo: instalación de la librería NumPy
```python
pip install numpy
```
---
## Importar la librería en un archivo Python
Después de instalar la librería, se puede utilizar dentro de un archivo `.py`
```python
import numpy
```

