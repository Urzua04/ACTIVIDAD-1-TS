#Trabajo supervisado - Introducción a la programación, sección: 17
#28/09/2023
#José Santiago Urzúa Luarca
#Objetivo: Crear un programa que muestre la secuencia de números en aumento o decremento utilizando bucles for y while.
#Entrada: No aplica

"""PROCESO
1. Utlizar ciclos.
2. Mostrar resultados.
"""
""" SALIDA
3. Mostrar secuencias de números según corresponda.
"""
# Usando ciclo for
print("Usando ciclo for para aumentar de 1 en 1: ")
for i in range(1, 26):
    print(i, end=", ")
print() 
print()


# Usando ciclo while
print("Usando ciclo while para aumentar de 1 en 1: ")
i = 1
while i <= 25:
    print(i, end=", ")
    i += 1
print() 
print()


# Usando ciclo for
print("Usando ciclo for para aumentar de 5 en 5: ")
for i in range(5, 51, 5):
    print(i, end=", ")
print() 
print()


# Usando ciclo while
print("Usando ciclo while para aumentar de 5 en 5: ")
i = 5
while i <= 50:
    print(i, end=", ")
    i += 5
print()
print()


# Usando ciclo for
print("Usando ciclo for para decrementar de 2 en 2: ")
for i in range(20, -1, -2):
    print(i, end=", ")
print()
print()


# Usando ciclo while
print("Usando ciclo while para decrementar de 2 en 2: ")
i = 20
while i >= 0:
    print(i, end=", ")
    i -= 2
print()



