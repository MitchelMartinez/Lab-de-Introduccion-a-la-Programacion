# 🔐 Sistema de Inicio de Sesión en Python

## 📌 Descripción General

El siguiente programa implementa un sistema básico de autenticación que permite al usuario ingresar un nombre de usuario y una contraseña, validando que cumplan con ciertos requisitos antes de permitir el acceso al sistema.

El sistema permite un máximo de tres intentos antes de finalizar el programa.

---

## 🔄 Control de Intentos

```python
intentos = 0

while intentos < 3:
```

Se inicializa la variable `intentos` en 0 para llevar el conteo de accesos fallidos.

El ciclo `while` permite que el usuario tenga un máximo de 3 intentos para ingresar correctamente sus credenciales. Mientras el número de intentos sea menor que 3, el programa seguirá solicitando los datos.

---

## 👤 Entrada de Datos

```python
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
```

Se solicita al usuario que ingrese su nombre de usuario y contraseña, los cuales se almacenan en las variables `usuario` y `contraseña`.

---

## ✅ Validación del Usuario

### 🔹 Usuario no vacío

```python
if usuario == "":
```

Se verifica que el campo usuario no esté vacío. En caso de estarlo, se incrementa el número de intentos y se reinicia el ciclo mediante `continue`.

---

### 🔹 Usuario alfanumérico

```python
if not usuario.isalnum():
```

El método `isalnum()` permite validar que el usuario contenga únicamente letras y números, sin espacios ni caracteres especiales.

El uso de `not` indica que si el usuario no cumple esta condición, se considera inválido.

---

## 🔒 Validación de la Contraseña

### 🔹 Longitud mínima

```python
if len(contraseña) < 8:
```

Se valida que la contraseña tenga al menos 8 caracteres. Si no cumple con esta condición, se incrementa el número de intentos.

---

### 🔹 Presencia de letra y número

Se utilizan dos variables booleanas para determinar si la contraseña contiene al menos una letra y un número.

```python
tiene_letra = False
tiene_numero = False
```

Posteriormente, se recorre cada carácter de la contraseña:

```python
for elemento in contraseña:
    if elemento.isalpha():
        tiene_letra = True
    if elemento.isdigit():
        tiene_numero = True
```

- `isalpha()` verifica si el carácter es una letra.
- `isdigit()` verifica si el carácter es un número.

---

### 🔹 Validación final de la contraseña

```python
if not tiene_letra or not tiene_numero:
```

Se comprueba que la contraseña tenga al menos una letra y un número. Si alguna de estas condiciones no se cumple, el acceso será denegado.

---

## 🔑 Verificación de Credenciales

```python
if usuario == "admin" and contraseña == "Admin2026":
```

Se comparan los datos ingresados con las credenciales válidas almacenadas directamente en el código.

Si coinciden, se muestra un mensaje de acceso concedido y se finaliza el ciclo con `break`.

En caso contrario, se incrementa el contador de intentos.

---

## 🚫 Límite de Intentos

Si el usuario no logra ingresar correctamente sus credenciales en tres intentos, el programa finaliza mostrando un mensaje indicando que se alcanzó el número máximo de intentos.

---

## 🧠 Conceptos Utilizados

- Variables
- Ciclo `while`
- Condicionales `if`
- Operadores lógicos `and` y `or`
- Métodos de cadenas:
  - `isalnum()`
  - `isalpha()`
  - `isdigit()`
- Función `len()`
- Instrucciones `continue` y `break`
