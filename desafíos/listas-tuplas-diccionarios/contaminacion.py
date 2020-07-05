"""
1.Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 

"""

from random import randint

message = 'Indique del 1 al 10 cuanto conoce sobre la contaminación'

totalPeople = randint(2,7)

numbers = []

for value in range(0,totalPeople):
    num = int(input(f'{message}: '))
    numbers.append(num)

numbers.sort()

print(f"Lista ordenada: {numbers}")
    
