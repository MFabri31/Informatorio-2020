"""
Ejercicio 2: Nivel Fácil 
1.desarrollar un programa que solicite la cantidad de intentos fallidos de ingreso de una contraseña. si la cantidad es mayor a  5 veces, debes 
informar " cuenta bloqueada".

"""


user_name = input("Ingrese un nombre: ")
user_pass = input("Ingrese una contraseña: ")
confirm_pass = input("Confirme su contraseña: ")

count = 0

if user_pass == confirm_pass:
    print(f'{user_name}, ha iniciado sesión')

elif user_pass != confirm_pass:
    while count < 5:
        print('Las contraseñas no coinciden. intente nuevamente')
        confirm_pass = input("Confirme su contraseña:")
        if user_pass == confirm_pass:
            print(f'{user_name} has iniciado sesión correctamente')
            break
        count = count + 1
        print('Cuenta bloqueada. Intente más tarde')

    

    


