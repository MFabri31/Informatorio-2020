"""
Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.

Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos a la Central con el siguiente significado:

3 letras: Correspondientes a la patente.

Del valor numérico:
    -Los 3 primeros números corresponden a la patente
    -El 4 número indica
        1- Tiró basura a la vía pública
        0 - No tiró basura a la vía pública
    El 5 número indica
        1 - Ya había sido multado el vehículo
        0 - Vehículo sin multas.

Deberás informar total de vehículos observados, total de vehículos que han tirado basura y porcentaje de éstos que ya habían sido multados.

"""


total = []


while True:
    print("Sistema de monitoreo de patente")
    print("----Opciones----\n")
    option = input('a) Ingresar patente\nb) Terminar \n>')
    
    
    if option == 'a':
        print('ingresar')
        number = input("N° de patente: >  ")
        
        if number[3] == "1":
            print("Ha tirado basura a la vía pública")
        else:
            print("No ha tirado basura a la vía pública")
        if number[4] == "1":
            print("Vehículo ya multado")
        elif number[4] == "0":
            print("Vehículo sin multa")

        total.append(number)

    elif option == 'b':
        break
            
    print(' ')
    
print('-----------')
print('Informe')
print(f'Total de vehículos observados: {len(total)}')

total_garbage = 0
cars_fined = 0

for license_plate in total:
    if license_plate[3] == "1":
        total_garbage += 1
    if license_plate[4] == "1":
        cars_fined += 1
        
        
total = len(license_plate)
parcentage = float(cars_fined / total*100)


print(f'Total de vehículos que han tirado basura: {total_garbage}')
print(f'Porcentaje de vehículos ya multados: {cars_fined}%')
