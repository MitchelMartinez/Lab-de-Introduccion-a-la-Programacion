intentos = 0

while intentos < 3:
    print("Usuario")
    usuario = input("Ingrese su nombre de usuario: ")
    
    print("Contraseña")
    contraseña = input("Ingrese su contraseña: ")

    
    if usuario == "":
        print("El usuario no puede estar vacío.")
        intentos += 1
        continue

    if not usuario.isalnum():
        print("El usuario debe ser alfanumérico y sin espacios.")
        intentos += 1
        continue

    # Validación contraseña
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        intentos += 1
        continue

    tiene_letra = False
    tiene_numero = False

    for elemento in contraseña:
        if elemento.isalpha():
            tiene_letra = True
        if elemento.isdigit():
            tiene_numero = True

    if not tiene_letra or not tiene_numero:
        print("La contraseña debe contener al menos una letra y un número.")
        intentos += 1
        continue

    # Validación credenciales hardcode
    if usuario == "admin" and contraseña == "Admin2026":
        print("Acceso concedido ✅")
        break
    else:
        print("Credenciales incorrectas.")
        intentos += 1

if intentos == 3:
    print("Se alcanzó el número máximo de intentos. Programa terminado.")    
    




    





