"""
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:

    -Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
    -Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
    -Si ambos números son iguales, debe devolver el nombre de ambas.
"""


cityName1 = input('Nombre de ciudad 1:\n>').capitalize()
cityName2 = input('Nombre de ciudad 2:\n>').capitalize()

tons = []

for value in range(1,3):
    while True:
        try:
            tonsOfCity = int(input(f'Toneladas recicladas en ciudad {value}: \n>'))
            tons.append(tonsOfCity)
        except ValueError:
            print('Solo se admiten valores numéricos!')
        else:
            break

tonsOfCity1 = tons[0]
tonsOfCity2 = tons[1]


def relation(a,b):
    if a > b:
        print(f'Ciudad 1: {cityName1}')
    elif b > a:
        print(f'Ciudad 2: {cityName2}')
    elif  a == b:
        print('--------')
        print(f'Ciudades:\n1.{cityName1}\n2.{cityName2}')

relation(tonsOfCity1,tonsOfCity2)