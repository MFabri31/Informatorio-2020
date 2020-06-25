'''
Ejercicio 1:
Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas.

'''
# Coloque la resolución del Ejercicio debajo de esta línea


numbers = []

for value in range(1,11):
    numbers.append(value)

numbers.reverse()

print(f"Orden inverso:{numbers}")


'''
Ejercicio 2:
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa 
debe mostrar por pantalla las asignaturas que el usuario no aprobo y tiene que volver a cursar.

'''
# Coloque la resolución del Ejercicio debajo de esta línea

message = "Nombre de la asignatura"
message2 = "Nota de la asignatura"
warnMessage = "Materias que debes volver a cursar: "

subjects = []
approvedSubjects = []
totalSubjects = 5

count = 1

while count < totalSubjects:
    subjectName = input(f"{message} {count}: ").capitalize()
    subjects.append(subjectName)

    count += 1


for value in subjects:
    score = int(input(f"{message2} {value}:"))
    if score > 5:
        approvedSubjects.append(value)

for value in approvedSubjects:
    subjects.remove(value)


print(warnMessage)

for value in subjects:
    print(value)
