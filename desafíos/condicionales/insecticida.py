"""
Elaborar un programa en Python que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene usando insecticida en su plantación. 
Si hace 10 o más años, debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación". 
Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación".

"""


option = int(input("Ingrese los años que lleva usando insecticida:\n1) Hace 10 años o más\n2) Hace menos de 10 años.\n>"))

if option != 1 and option != 2:
    print('Ha ingresado una opción incorrecta. Vuelva a intentarlo.')
elif option == 1:
    print('Por favor solicite revisión de los suelos en su plantación.')
elif option == 2:
    print('Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos de tu platantación.')
