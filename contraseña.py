"""
Ejercicio 2: Nivel Fácil 
1.desarrollar un programa que solicite la cantidad de intentos fallidos de ingreso de una contraseña. si la cantidad es mayor a  5 veces, debes 
informar " cuenta bloqueada".

"""


successMessage = ("ha iniciado sesión.")
warnMessage = ("Las contraseñas no coinciden intente nuevamente.")
errorMessage= ("Cuenta Bloqueada. intente más tarde")

userName = input("Ingrese un nombre: ")
userPass = input("Ingrese una contraseña: ")
confirmPass = input("Confirme su contraseña: ")

count = 0

if userPass == confirmPass:
    print(userName, successMessage)

elif userPass != confirmPass:
    while count < 5:
        print(warnMessage)
        confirmPass = input("Confirme su contraseña:")
        if userPass == confirmPass:
            print(userName,successMessage)
            break
        count = count + 1
        print(errorMessage)

    


