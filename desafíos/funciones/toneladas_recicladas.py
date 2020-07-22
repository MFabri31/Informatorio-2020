"""
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:

    -Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
    -Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
    -Si ambos números son iguales, debe devolver el nombre de ambas.
"""


city_name1 = input('Nombre de ciudad 1:\n>').capitalize()
city_name2 = input('Nombre de ciudad 2:\n>').capitalize()

tons = []


for value in range(1,3):
    while True:
        try:
            tons_of_city = int(input(f'Toneladas recicladas en ciudad {value}: \n>'))
            tons.append(tons_of_city)
        except ValueError:
            print('Solo se admiten valores numéricos!')
        else:
            break


tons_of_city1 = tons[0]
tons_of_city2 = tons[1]


def relation(a,b):
    if a > b:
        print(f'Ciudad 1: {city_name1}')
    elif b > a:
        print(f'Ciudad 2: {city_name2}')
    elif  a == b:
        print('--------')
        print(f'Ciudades:\n1.{city_name1}\n2.{city_name2}')

        
relation(tons_of_city1,tons_of_city2)
