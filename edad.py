"""
Ejercicio 1: Nivel Fácil 

Solicitar la edad de una persona e informar si es mayor de edad o no

"""

successMessage = "La persona es mayor de edad."
warnMessage = "La persona es menor edad."

personAge = int(input("Por favar ingrese la edad de una persona."))


if personAge < 18:
    print(warnMessage)
else:
    print(successMessage)

