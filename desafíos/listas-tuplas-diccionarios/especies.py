"""
Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.
Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición i.
"""


species = ('Camaleón de hoja','Panda rojo','Rinoceronte','Leopardo de las nieves','Elefante asiático')

p = 1
n = 4

for i in species[p:n]:
    print(f'Hola soy un {i} cúidame.')
