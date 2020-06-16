"""
Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:

    -Tamaño Normal: Mensaje "Pez en buenas condiciones"
    -Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
    -Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
    -Tamaño sobredimensionado: Mensaje "Pez contaminado"

"""

welcomeMessage = "A continuación necesitamos que nos indique el tamaño del pez para saber si está contaminado o no."
warnMessage = "Has ingresado un valor inválido. Por favor vuelva a intentarlo."



print(welcomeMessage)

fishSize = (input("Tamaño del pez: a) Normal b) Por debajo del normal c) Un poco por encima de lo normal D) Pez contaminado."))
fishSize = fishSize.lower()

if fishSize == "a":
    print("Pez en buenas condiciones.")
elif fishSize == "b":
    print("Pez con problemas de nutrición.")
elif fishSize == "c":
    print("Pez con síntomas de organismo contaminado.")
elif fishSize == "d":
    print("Pez contaminado.")
else:
    print(warnMessage)





