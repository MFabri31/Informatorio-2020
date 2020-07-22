"""
1.Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 

"""
from random import randint

numbers = []

total_people = randint(2,7)

for value in range(0,total_people):
    num = int(input('Indique del 1 al 10 cuanto conoce sobre la contaminación: '))
    numbers.append(num)


numbers.sort()

print(f"Lista ordenada: {numbers}")
