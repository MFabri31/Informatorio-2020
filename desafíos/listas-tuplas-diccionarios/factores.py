"""
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el número esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.

"""

factors = (' ','Aguas residuales','Sustancias químicas','plásticos','Cambio climático')

while True:
    number = int(input("Digíte un n°: "))

    if number > 4:
        print('Contenido no disponible')
    elif number == 0:
        break
    else:
        print(factors[number])
