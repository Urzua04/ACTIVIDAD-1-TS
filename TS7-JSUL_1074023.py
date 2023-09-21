#Trabajo supervisado - Introducción a la programación, sección: 17
#21/09/2023
#José Santiago Urzúa Luarca
#Objetivo: Crear un programa que solicite al usuario ingresar un número dentro del rango de 1 a 10 y verificar si está en el rango correcto. Ademas, este programa debe mostrar la tambla de multiplicar del número indicado.
#Entrada: numero, ingrese
"""PROCESO
1. Mostrar mi nombre completo
2. Solicitar al usuario el ingreso de un número entre el 1 y 10.
3. Verificar número.
4. Mostrar resultados.
"""
""" SALIDA
4. Mostrar tabla de multiplicar y pregunta para continuar.
"""
# Mostrar nombre completo
print("Mi nombre es José Santiago Urzúa Luarca")

while True:
    #Declarar variables y pedir datos:
    numero = int(input("Por favor, ingrese un número entre 1 y 10: "))

    #Verificar que el número esté en el rango correcto
    if 1 <= numero <= 10:
     
    #Mostrar resultados:
        for i in range (1,11):
            resul = numero * i
            print (resul)
    ingrese = input("¿Desea realizar un nuevo ingreso?")
    if ingrese == "no":
       break


        
