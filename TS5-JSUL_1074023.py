#Trabajo supervisado - Introducción a la programación, sección: 17
#07/09/2023
#José Santiago Urzúa Luarca
#Objetivo: Crear un programa que solicite al usuario información personal.
#Entrada: sNombre,sEdad, sCarrera, sCarne
"""PROCESO
1. Solicitar al usuario sus datos personales y almacenarlos.
2. Mostrar los resultados.
"""
""" SALIDA
3. Mostrar nombre, edad, carrera y carné.Er
"""
print("Mi segundo programa")

#Declarar variables y pedir datos:
sNombre=str(input("Ingrese su nombre: "))
sEdad=str(input("Ingrese su edad: "))
sCarrera=str(input("Ingrese la carrera que está cursando: "))
sCarné=str(input("Ingrese su No. de carné de estudiante: "))

#Mostrar resultados:
print("Nombre: "+sNombre)
print("Edad: "+sEdad)
print("Carrera: "+sCarrera)
print("Carné: "+sCarné)

print("Soy "+sNombre+", tengo "+sEdad+" años y estudio la carrera de "+sCarrera+".")
print("Mi número de carné es;: "+sCarné)