"""
Estudiantes de un curso se han dividido en dos grupos A y B de acuerdo al turno y el nombre. 
El grupo A está formado por estudiantes del turno Tarde con un nombre anterior a la M y estudiantes del turno Noche con un nombre posterior a la N y el grupo B por el resto.

Escribir un programa que pregunte al usuario su nombre y turno, y muestre por pantalla el grupo que le corresponde.

"""


print('A continuación ingrese su nombre y el turno al que asiste para conocer a que grupo pertenece.')

student_name = input("Nombre: ").capitalize()
student_turn = input("Turno: ").capitalize()


if student_name < "m" and student_turn == "tarde":
    print("Usted pertenece al grupo A.")
elif student_name > "n" and student_turn == "noche":
    print("Usted pertenece al grupo A.")
else:
    print("Usted pertenece al grupo B.")
 


