"""
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas. Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas.

"""

people_100 = 0
people_200 = 0
people_300 = 0


while True:
    try:
        total_people = int(input('Ingrese el total de personas que han recolectado colillas: \n> '))
    except ValueError:
        print('Error! Solo se permite el ingreso valores numéricos.')
        print('')
    else:
        break
        
        
for value in range(0,total_people):
    value += 1
    
    while True:
        try:
            cigarette_butts = int(input(f'Persona n°{value} colillas recolectadas:\n> '))
        except ValueError:
            print('Debe ingresar un valor numérico.')
            print('')
        else:
            break
            
            
    if cigarette_butts < 100:
        people_100 = people_100 + 1
        
    elif cigarette_butts < 200:
        people_200 = people_200 + 1
    else:
        people_300 = people_300 + 1
        
        
    percentage_100 = round((people_100 / total_people) * 100)
    percentage_200 = round((people_200 / total_people) * 100)
    percentage_300 = round((people_300 / total_people) * 100)  
    
    
print(f'Total de personas: {total_people}')
print(f'Menos de 100 colillas: {people_100} / Porcentaje {percentage_100}%')
print(f'Mas de 100 y menos de 200 colillas: {people_200} / Porcentaje {percentage_200}%')
print(f'Mas de 300 colillas: {people_300} / Porcentaje {percentage_300}%')
