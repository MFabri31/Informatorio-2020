"""
150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 
Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle,
e imprima la cantidad de años que tarda en degradarse.

"""

import time


while True:
    print('Indique un tipo de elemento para conocer los años que tarda en degradarse:')
    print('---Opciones---')
    try:
        option = input('a) Bolsa de plástico\nb) Botella de PET\nc) Envase de tetrabrik\nd) Chicle. \n>').lower()      
        if option != 'a' and option != 'b' and option != 'c' and option != 'd':
            raise ValueError('Opción no contemplada. Intente nuevamente')
    except ValueError as Error:
        print(Error)
        print('')
        time.sleep(1.5)
    else:
        break
        

def element(element):
    if element == 'a':
        print(f"Tipo de elemento: Bolsa de plástico\nTiempo que tarda en degradarse: 150 años.")  
    elif element == 'b':
        print(f"Tipo de elemento: Botella de PET:\n Tiempo que tarda en degradarse: 1000 años.")  
    elif element == 'c':
        print(f"Tipo de elemento Envase de tetrabik:\n Tiempo que tarda en degradarse: 30 años.")  
    elif element == 'd':
        print(f"Tipo de elemento: Chicle\nTiempo que tarda en degradarse: 5 años.")
   

element(option)