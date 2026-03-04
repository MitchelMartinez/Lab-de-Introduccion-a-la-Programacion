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
                clasificar = 0
                while clasificar == 0:                    
                    numero = (input("Ingrese un numero entero: "))
                    if type(numero) == str and numero.lstrip("-").isdigit():
                        numero = int(numero)
                        if numero == 0:
                            print("El numero es cero.")
                            clasificar = 1
                        else:
                            if numero > 0:
                                print("El numero es positivo.")    
                            elif numero < 0:
                                print("El numero es negativo.")
       
                        if numero % 2 == 0 and numero != 0:
                                print("El numero es par.")
                        elif numero % 2 != 0 and numero !=0:
                            print("El numero es impar.")
                        clasificar = 1
                    else:
                        print("El valor ingresado no es un numero entero. Intente nuevamente.")
                        continue
                    if clasificar == 1:
                        print("¿Desea clasificar otro numero? (s/n)")
                        respuesta = input().lower()
                        if respuesta == 's':
                            clasificar = 0
                        else:
                            break


            elif opcion == "2":
                print("Categoria de Edad y permisos.")
                print("Ingrese su edad (0 a 120)")
                edad = int(input())
                print("Cuenta con identificacion oficial? (s/n)")
                identificacion = input().lower()
                print("Cuenta con licencia de conducir? (s/n)")
                licencia = input().lower()
               
                if edad > 0 and edad <12:
                    print("Eres un niño.")
                elif edad > 12 and edad < 18:
                    print("Eres un adolescente.")
                elif edad > 18 and edad < 64:
                    print("Eres un adulto.")
                elif edad > 64 and edad < 120:
                    print("Eres un adulto mayor.")  
                else:
                    print("Como sigues vivo?")
               
                if edad >= 13:
                    print("Puedes registrarte")
                elif edad >= 13 and edad < 18:
                    print("Puedes comprar con un tutor")
                else:
                    print("Puedes comprar sin tutor")
                if edad >= 18 and licencia == "s":
                    print("Puedes conducir")
                elif edad >= 21 and identificacion == "s":
                    print("Puedes comprar servicio VIP")

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
