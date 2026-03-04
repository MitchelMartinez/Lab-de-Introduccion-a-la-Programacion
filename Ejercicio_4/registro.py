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

    
    if usuario == "admin" and contraseña == "Admin2026":
        print("Acceso concedido ✅")
        acceso = 1
        while acceso == 1:
            print("\nMenú de opciones:")
            print("1. Clasificar numero")
            print("2. Categoria de Edad y permisos")
            print("3. Calcular tarifa")
            print("4. Cerrar sesion")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print("Clasificar numero.")
            elif opcion == "2":
                print("Categoria de Edad y permisos.")
            elif opcion == "3":
                print("Calcular tarifa.")
            elif opcion == "4":
                print("Cerrar sesion.")
                acceso = 0
            elif opcion == "5":
                print("Saliendo del menú...")
                intentos = 4
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                continue 
        
    else:
        print("Credenciales incorrectas.")
        intentos += 1

if intentos == 3:
        print("Numero de intentos agotados.")    
elif intentos == 4:
        print("Saliendo del sistema...")
