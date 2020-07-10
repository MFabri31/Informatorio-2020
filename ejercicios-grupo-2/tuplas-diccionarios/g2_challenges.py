'''
Ejercicio 1:
Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
'''
# Coloque la resolución del Ejercicio debajo de esta línea



# En este ejercicio logre encontrar 2 soluciones 

# Solución 1

from random import randint

listOfNumbers = []

for value in range(1,11):
    number = randint(1,20)
    listOfNumbers.append(number)

numbers = tuple(listOfNumbers)

print(f'Tupla: {numbers}')

num = int(input("Ingrese un numero: "))

if num not in numbers:
    print(f'El número ingresado {num} no se encuentra en la tupla.')
else:
    total = numbers.count(num)
    print(f'El número ingresado {num} se repite {total} veces.')


# Solución 2

# numbers = (1,1,2,2,3,4,5,5,6,6,7,8,9,9,9,10)

# num = int(input("Ingrese un numero: "))

# if num not in numbers:
#     print(f'Tupla: {numbers}')
#     print(f'El número ingresado {num} no se encuentra en la tupla.')
# else:
#     total = numbers.count(num)
#     print(f'Tupla: {numbers}')
#     print(f'El número ingresado {num} se repite {total} veces.')


'''
Ejercicio 2:
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
# Coloque la resolución del Ejercicio debajo de esta línea

divisas = {
    'Euro': '€',
    'Dollar':'$',
    'Yen': '¥'
}

divisa = input("Ingrese un tipo de divisa: ").capitalize()

if divisa not in divisas:
    print(f"La divisa ingresada {divisa} no se encuentra en el diccionario.")
else:
    print(f"La divisa ingresada {divisa } se encuentra en el diccionario.")


'''
Ejercicio 3:Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en 
el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario 
por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, 
(5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.

'''
# Coloque la resolución del Ejercicio debajo de esta línea

clients = {}
dataClient = {}


while True:
    print('------Menu------')
    option = int(input('1) Añadir cliente\n2) Eliminar cliente\n3) Mostrar cliente\n4) Listar todos los clientes\n5) Listar clientes preferentes\n6) Terminar\n>'))

    if option == 1:
        nif = int(input('Ingrese su NIF: '))
        name = input('Ingrese su nombre: ').capitalize()
        address = input('Indique su direccion: ').capitalize()
        numberPhone = input('Indique su n° de telefono: ')
        email = input('Ingrese su correo: ').lower()
        preferential = input('Indique si es cliente preferente [S/N]: ').lower()
        
        if preferential == 's':
            preferential = True
        elif preferential == 'n':
            preferential = False
        
        dataClient = {
            'Nombre': name,
            'Direccion':address,
            'Telefono': numberPhone,
            'Correo':email,
            'Preferente': preferential
        }

        clients[nif] = dataClient
    
    elif option == 2:
        removeClient = int(input('Indique el NIF del cliente que desea eliminar:\n>')) 

        while removeClient not in clients:
            print('El n° de nif que ha ingresado no se encontrado. Intente nuevamente.')
            removeClient = int(input('Indique el NIF del cliente que desea eliminar: ')) 
        
        if removeClient in clients:
            del clients[removeClient]

    elif option == 3:
        showClient = int(input('Indique el NIF del cliente que desea mostrar: '))
        
        while showClient not in clients:
            print('El n° de nif que ha ingresado no se ha encontrado. Intente nuevamente.')
            showClient = int(input('Indique el NIF del cliente que desea mostrar: '))
        
        if showClient in clients:
            print(f'Clinte: {clients[showClient]}')
          
        
    elif option == 4:
        print(f"Clientes:\n{clients} ")
        
    elif option == 5:
        for key, value in clients.items():
            if value['Preferente']:
                print('Clientes Preferentes: ')
                print(f'NIF:{key} - Cliente: {value["Nombre"]}')
           
    
    elif option == 6:
        break
