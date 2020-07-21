"""
Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:

    -Tamaño Normal: Mensaje "Pez en buenas condiciones"
    -Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
    -Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
    -Tamaño sobredimensionado: Mensaje "Pez contaminado"

"""

print('Necesitamos que nos indique el tamaño del pez para saber si está contaminado o no.')

fish_size = (input("Tamaño del pez:\na) Normal\nb) Por debajo del normal\nc) Un poco por encima de lo normal\nD) Pez contaminado.\n>"))
fish_size = fish_size.lower()

if fish_size == "a":
    print("Pez en buenas condiciones.")
elif fish_size == "b":
    print("Pez con problemas de nutrición.")
elif fish_size == "c":
    print("Pez con síntomas de organismo contaminado.")
elif fish_size == "d":
    print("Pez contaminado.")
else:
    print('Has ingresado un valor inválido. Por favor vuelva a intentarlo.')



