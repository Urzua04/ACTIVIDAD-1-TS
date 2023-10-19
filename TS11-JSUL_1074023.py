# Introducción a la programación - Sección 017
# Fecha: 19 de octubre de 2023
# Autor: José Santiago Urzúa Luarca
# Descripción: Este programa crea un programa que solicite al usuario una palabra, 
# mostrar las primeras tres letras de esa palabra, almacenarlas en una nueva cadena, 
# pedir un nuevo texto al usuario, y reemplazar todas las vocales "O" con "X" en el 
# texto si existen, informando si no se encontraron "O"s en el texto.

"""PROCESO
El programa solicita al usuario que ingrese una palabra.
Muestra las primeras tres letras de la palabra una a una.
Almacena las primeras tres letras en una nueva cadena.
Solicita al usuario que ingrese una nueva palabra.
Reemplaza las vocales "O" con la letra "X" en el texto, si existen "O" en el texto.
Si el texto no contiene "O", muestra un mensaje de que no se realizaron modificaciones.
"""
"""
Salida:
El programa proporciona una variedad de salidas en función del flujo de ejecución, 
que incluyen la visualización de letras individuales de la palabra ingresada, la nueva 
subcadena formada y el texto modificado (si corresponde), así como mensajes informativos.
"""

# Pedir al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Mostrar las primeras tres letras una a una
print("Las primeras tres letras de la palabra ingresada son:")
for i in range(3):
    print(palabra[i])

# Almacenar las primeras tres letras en una nueva cadena
NuevaSubcadena = palabra[:3]
print("Nueva subcadena:", NuevaSubcadena)

# Pedir al usuario una nueva palabra
texto = input("Ingrese una nueva palabra: ")

# Reemplazar las vocales "O" con la letra "X" solo si hay "O" en el texto
if "O" in texto or "o" in texto:
    textoMod = texto.replace("O", "X").replace("o", "X")
    print("Texto modificado:", textoMod)
else:
    print("El texto no contiene la letra 'O'. No se realizaron modificaciones.")


"""
Investgación
Python proporciona varias funciones integradas en su biblioteca estándar para ayudar a manipular cadenas de muchas maneras diferentes.
split(): esta función se utiliza para dividir una cadena en una lista de subcadenas según un separador específico. Por ejemplo, si tenemos una cadena "¡Hola mundo!" y queremos dividirlo en dos subcadenas "Hola" y "Mundo!", podemos usar la función split() con el separador ",". La sintaxis de la función split() es la siguiente:
cadena.split(separador, maxsplit)

separador: este es el carácter o secuencia de caracteres que se utiliza para dividir la cadena. Si no se especifica ningún separador, se utiliza cualquier carácter de espacio en blanco como separador.
maxsplit: este es un parámetro opcional que especifica el número máximo de divisiones que se realizarán. Si no se especifica, todas las apariciones del separador se utilizan para dividir la cadena.
join(): esta función se utiliza para unir una lista de cadenas en una sola cadena usando un separador específico. Por ejemplo, si tenemos una lista de cadenas ["Hola", "¡Mundo!"] y queremos unirlas en una sola cadena "¡Hola, Mundo!", podemos usar la función join() con el separador ", ". La sintaxis de la función join() es la siguiente:
separador.unir(iterable)

separador: Este es el carácter o secuencia de caracteres que se utiliza para unir las cadenas.
iterable: esta es la lista de cadenas que se van a unir.

A continuación se presentan tres situaciones en un programa en las que sería conveniente utilizar estas funciones:
Análisis de un archivo CSV: al leer un archivo CSV, podemos usar la función split() para dividir cada línea en una lista de valores basada en el separador de coma. Esto facilita el acceso a cada valor de la línea como un elemento separado en la lista.
Unir componentes de ruta: cuando trabajamos con rutas de archivos, podemos usar la función join() para unir los componentes de la ruta en una sola cadena de ruta usando el separador apropiado para el sistema operativo. Por ejemplo, en Windows, el separador es "", mientras que en los sistemas basados en Unix, el separador es "/".
Formato de cadenas: al construir una cadena a partir de múltiples valores, podemos usar la función join() para concatenar los valores en una sola cadena usando un separador específico. Esto se usa a menudo en declaraciones de registro o depuración para crear un mensaje formateado que incluye valores variables.
"""
