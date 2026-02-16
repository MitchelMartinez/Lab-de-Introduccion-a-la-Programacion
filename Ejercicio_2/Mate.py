def convertir_base(numero, base):
    if numero == 0:
        return "0"
    
    digitos = "0123456789ABCDEF"
    resultado = ""
    
    while numero > 0:
        residuo = numero % base
        resultado = digitos[residuo] + resultado
        numero = numero // base
    
    return resultado


valor = input("Ingresa un valor (int, float, True, False): ")

if valor.lower() == "true":
    numero = 1
elif valor.lower() == "false":
    numero = 0
else:
    try:
        if "." in valor:
            numero = int(float(valor)) 
        else:
            numero = int(valor)
    except:
        print("Entrada no válida")
        exit()


print("\nNúmero en decimal:", numero)
print("Binario:", convertir_base(numero, 2))
print("Octal:", convertir_base(numero, 8))
print("Hexadecimal:", convertir_base(numero, 16))
