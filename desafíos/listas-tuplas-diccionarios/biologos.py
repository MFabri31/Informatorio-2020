"""
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). 
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.

"""

biologists = {}

flag = True

while flag:
    addContact = input('Agregar contacto [S/N]: ')
    
    if addContact == 'n':
        print('Cerrando...')
        flag = False
    elif addContact == 's':
        name = input('Nombre: ').capitalize()
        email = input('Email: ')
        if name not in biologists:
            biologists[name] = email
        else:
            print('Este nombre ya se encuentra agendado.')
          
    

print(f'Contactos: {biologists}')





