"""
DESAFÍO 4

Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6

"""


# importo la libreria sty para generar los casilleros de colores
from sty import bg, rs
    
locker = '   ' 

for i in range(1,4):

    print('')
    for value in range(1,5):
        print(bg.da_green ,end=locker + bg.rs)
        for value in range(1,2,1):
            print(bg.li_white ,end=locker + bg.rs)
    
    print('')
    for value in range(1,5):
        print(bg.li_white ,end=locker + bg.rs)
        for value in range(1,2,1):
            print(bg.da_green ,end=locker + bg.rs)

    