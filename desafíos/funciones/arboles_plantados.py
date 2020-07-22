"""
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.
"""

total_trees = []


def getData():
    while True:
        try:
            total_cities = int(input('Indique el total de ciudades que han plantados árboles: \n>'))
        except ValueError:
            print('Error! debes ingresar un valor numérico. Intente nuevamente.')
        else:
            break

    for value in range(0,total_cities):
         value += 1
         trees = int(input(f'Árboles plantados en la ciudad {value}: \n> '))
         total_trees.append(trees)


getData()


def divide(total_trees):
    list1 = []
    list2 = []

    city = 0

    for value in total_trees:
        if value > 100:
           list1.append(value)
           city += 1
        elif value < 100:
            list2.append(value)
            
    return list1,list2,city


list1,list2,city = divide(total_trees)  


print('------------')


print(f'Lista 1 con mas de 100 árboles: {list1}')
print(f'Lista 2 con el resto de árboles: {list2}')
print(f'Total de ciudades que han plantado mas de 100 árboles: {city}')
