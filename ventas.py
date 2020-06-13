"""
Ejercicio 4: Nivel Medio
Desarrollar un programa que solicite que te ingresen las ventas de 2 días. Y luego informe por pantalla si se vendió más el día 1, el día 2, o si se vendió lo mismo en ambos días.

"""


day1 = int(input("Ingrese el total de ventas del día 1: "))
day2 = int(input("Ingrese el total de ventas del día 2: "))


if day1 == day2:
    print("Las ventas fueron iguales en ambos días.")
elif day1 > day2:
    print("Las ventas del día 1 fueron mayores a las del día 2.")
elif day2 > day1:
    print("Las ventas del día 2 fueron mayores a las del día 1.")
