"""
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas. Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas.

"""

people100 = 0
people200 = 0
people300 = 0


while True:
    try:
        totalPeople = int(input('Ingrese el total de personas que han recolectado colillas: \n> '))
    except ValueError:
        print('Error! Solo se permite el ingreso valores numéricos.')
        print('')
    else:
        break


for value in range(0,totalPeople):
    value += 1
    
    while True:
        try:
            cigaretteButts = int(input(f'Persona n°{value} colillas recolectadas:\n> '))
        except ValueError:
            print('Debe ingresar un valor numérico.')
            print('')
        else:
            break

    
    if cigaretteButts < 100:
        people100 = people100 + 1
        
    elif cigaretteButts < 200:
        people200 = people200 + 1
    else:
        people300 = people300 + 1

    percentage100 = round((people100 / totalPeople) * 100)
    percentage200 = round((people200 / totalPeople) * 100)
    percentage300 = round((people300 / totalPeople) * 100)  



print(f'Total de personas: {totalPeople}')
print(f'Menos de 100 colillas: {people100} / Porcentaje {percentage100}%')
print(f'Mas de 100 y menos de 200 colillas: {people200} / Porcentaje {percentage200}%')
print(f'Mas de 300 colillas: {people300} / Porcentaje {percentage300}%')