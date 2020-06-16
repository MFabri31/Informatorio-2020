"""
Elaborar un programa en Python que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene usando insecticida en su plantación. 
Si hace 10 o más años, debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación". 
Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".

"""

helpMessage = "Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos de tu platantación."
warnMessage = "Por favor solicite revisión de los suelos en su plantación."
errorMessage = "Has ingresado una opción incorrecta. vuelva a intentarlo."

question = int(input("Ingrese los años que lleva usando insecticida: 1) Hace 10 años o más  2) Hace menos de 10 años."))


if question != 1 and question != 2:
    print(errorMessage)
elif question == 1:
    print(warnMessage)
elif question == 2:
    print(helpMessage)
