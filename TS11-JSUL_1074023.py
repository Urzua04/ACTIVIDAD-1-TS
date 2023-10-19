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


