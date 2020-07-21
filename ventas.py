"""
Ejercicio 4: Nivel Medio
Desarrollar un programa que solicite que te ingresen las ventas de 2 días. Y luego informe por pantalla si se vendió más el día 1, el día 2, o si se vendió lo mismo en ambos días.

"""


day_1 = int(input("Ingrese el total de ventas del día 1:\n> "))
day_2 = int(input("Ingrese el total de ventas del día 2:\n> "))


if day_1 == day_2:
    print("Las ventas fueron iguales en ambos días.")
elif day_1 > day_2:
    print("Las ventas del día 1 fueron mayores a las del día 2.")
elif day_2 > day_1:
    print("Las ventas del día 2 fueron mayores a las del día 1.")
