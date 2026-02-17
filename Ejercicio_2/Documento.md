## Explicación del código

La primera línea de código indica la creación de una función llamada `convertir_base`, la cual recibe dos parámetros: `numero`, que es el valor que se va a convertir, y `base`, que indica a qué sistema de numeración se desea convertir dicho número. En este programa se utilizarán las bases 2, 8 y 16, correspondientes a binario, octal y hexadecimal.

Dentro de la función se inicia con una condición `if` que verifica si el número es igual a cero. En caso de que lo sea, retorna directamente el valor "0", evitando así errores en el proceso de conversión.

Después se crea una cadena llamada `digitos`, que contiene los símbolos necesarios para representar los residuos obtenidos durante la conversión, especialmente en el caso hexadecimal donde los valores del 10 al 15 se representan con las letras A hasta la F.

Posteriormente se crea la variable `resultado`, donde se irán almacenando los residuos obtenidos en cada iteración del proceso.

El ciclo `while` indica que el proceso de conversión se repetirá mientras la variable `numero` sea mayor que cero.

Dentro del ciclo se crea la variable `residuo`, la cual almacena el resultado del módulo entre el número y la base. Este residuo se utiliza como índice para buscar su símbolo correspondiente dentro de la cadena `digitos`, y se agrega al inicio de la variable `resultado`.

Después se realiza una división entera del número entre la base para continuar con el proceso de conversión. Este ciclo se repite hasta que el número deja de ser mayor que cero, momento en el cual termina el proceso.

Posteriormente, mediante la función `input`, se solicita un valor al usuario, el cual es recibido en forma de cadena de texto, pudiendo representar un entero, un número decimal o un valor booleano.

Mediante una estructura condicional `if`, si el usuario ingresa el valor "true", se asigna el valor entero 1 a la variable `numero`. De igual forma, si se ingresa "false", se asigna el valor 0.

En caso de no cumplirse estas condiciones, se pasa a una estructura `else` donde se utiliza un bloque `try`. Dentro de este bloque, se verifica si la cadena contiene un punto decimal. Si es así, se realiza una conversión en una sola línea utilizando `int(float(valor))`, donde primero se convierte el valor a tipo float y posteriormente a entero, eliminando la parte decimal.

Si no contiene punto decimal, se convierte directamente a entero mediante `int(valor)`. En caso de que estas conversiones no sean posibles, como al ingresar texto no numérico, se ejecuta el bloque `except`, mostrando un mensaje de entrada inválida y finalizando el programa.

Finalmente, las últimas líneas muestran los resultados en pantalla mediante `print`, donde se llama a la función `convertir_base` utilizando el número ingresado y las bases 2, 8 y 16, obteniendo así sus equivalentes en binario, octal y hexadecimal, además de mostrar su valor en decimal.

