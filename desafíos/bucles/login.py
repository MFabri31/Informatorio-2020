"""
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 

"""

userPass = "1234"
count = 1


loginPass = input("Ingrese su contraseña.")

if loginPass == userPass:
    print('')
elif loginPass != userPass:

    while count < 5:
        print('Las contraseña no coinciden, por favor vuelva intentarlo.')
        loginPass = input("Ingrese su contraseña.")
        
        if userPass == loginPass:
            print('Has iniciado sesion correctamente.')
    
            break
        count += 1       
    else:
        print('Has alcanzado el limite de intentos de login. Por favor intente mas tarde.')
