"""
Estudiantes de un curso se han dividido en dos grupos A y B de acuerdo al turno y el nombre. 
El grupo A está formado por estudiantes del turno Tarde con un nombre anterior a la M y estudiantes del turno Noche con un nombre posterior a la N y el grupo B por el resto.

Escribir un programa que pregunte al usuario su nombre y turno, y muestre por pantalla el grupo que le corresponde.

"""

welcomeMessage = "A continuación ingrese su nombre y el turno al que asiste para conocer a que grupo pertenece."
print(welcomeMessage)

studentName = input("Nombre: ")
studentTurn = input("Turno: ")

studentName = studentName.lower()
studentTurn = studentTurn.lower()

if studentName < "m" and studentTurn == "tarde":
    print("Usted pertenece al grupo A.")
elif studentName > "n" and studentTurn == "noche":
    print("Usted pertenece al grupo A.")
else:
    print("Usted pertenece al grupo B.")
 


