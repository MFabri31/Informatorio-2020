"""
Crea una tupla con los factores que más afectan a los mares. 

Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el número esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.

"""

factors = (' ','Aguas residuales','Sustancias químicas','plásticos','Cambio climático')

flag = True 

while flag:
    num = int(input("Digíte un n°: "))

    if num > 4:
        print('Contenido no disponible')
    elif num == 0:
        flag = False
    else:
        print(factors[num])

