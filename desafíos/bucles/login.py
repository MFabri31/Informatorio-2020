"""
Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 

"""

user_pass = "1234"
count = 1


login_pass = input("Ingrese su contraseña.\n>")

if login_pass == user_pass:
    print('Ha iniciado sesión correctamente')
elif login_pass != user_pass:

    while count < 5:
        print('Las contraseña no coinciden, por favor vuelva intentarlo.')
        login_pass = input("Ingrese su contraseña.")
        
        if user_pass == login_pass:
            print('Has iniciado sesion correctamente.')
    
            break
        count += 1       
    else:
        print('Has alcanzado el limite de intentos de login. Por favor intente mas tarde.')
