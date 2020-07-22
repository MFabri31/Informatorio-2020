''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    Escribir un programa que pida al usuario su peso (en kg) y 
    estatura (en metros), calcule el índice de masa corporal y 
    lo almacene en una variable, y muestre por pantalla la frase 
    "Tu índice de masa corporal es <imc>"
    donde <imc> es el índice de masa corporal calculado redondeado 
    con dos decimales.
'''
# Coloque la resolución del Ejercicio 1 debajo de esta línea

import math

print("Ingrese su peso en kg y su estatura en metros para conocer su imc.")

weight = float(input("Peso: "))
height = float(input("Estatura: "))

imc = round(weight / math.pow(height,2),2)

print(f"Tu índice de masa corporal es de: {imc}")

'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    Dadas dos edades ingresadas por pantalla, mostrar en pantalla si 
    la edad ingresada por dos usuarios es la misma. Además verificar
    para ambas edades si son mayores o menores de edad usando True o False
    e imprimir por pantalla un mensaje indicando si es mayor o menor.
'''
# Coloque la resolución del Ejercicio 2 debajo de esta línea

user1 = int(input("Por favor ingrese su edad: "))               
user2 = int(input("Ingrese su edad edad: "))

if user1 != user2 and (user1 >= 18 and user2 >= 18) and (user1 > user2):      
    print("Las edades de los usuarios no coinciden")
    print(f"Edad usuario 1: {user1}\nEdad usuario 2: {user2}") 
    print("Ambos usuarios son mayores. El usuario 1 es mayor")
    

elif user1 != user2 and (user1 >= 18 and user2 >= 18) and (user2 > user1):
       print("Las edades de los usuarios no coinciden")
       print(f"Edad usuario 1: {user1}\nEdad usuario 2:{user2}")
       print("Ambos usuarios son mayores. El usuario 2 es mayor")        

    
elif user1 != user2 and (user1 < 18 and user2 < 18) and (user1 > user2):
       print("Las edades de los usuarios no coinciden")
       print(f"Edad usuario 1: {user1}\nEdad usuario 2: {user2}")
       print("Ambos usuarios son menores. El usuario 1 es mayor")
       
elif user1 != user2 and (user1 < 18 and user2 < 18) and (user2 > user1):
       print("Las edades de los usuarios no coinciden")
       print(f"Edad usuario 1: {user1}\nEdad usuario 2: {user2}")
       print("Ambos usuarios son menores. El usuario 2 es mayor")
    
else:
    if user1 == user2 and (user1 >= 18 and user2 >= 18):
           print("Las edades de los usuarios son iguales")
           print(f"Edad usuario 1: {user1}\nEdad usuario 2: {user2}")
           print("Ambos usuarios son mayores")
      
    elif user1 == user2 and (user1 < 18 and user2 < 18):
           print("Las edades de los usuarios son iguales")
           print(f"Edad usuario 1: {user1}\nEdad usuario 2: {user2}")
           print("Ambos usuarios son menores")         
'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3: 
    Escribe un programa que dados dos números, uno real (base) 
    y un entero positivo (exponente), saque por pantalla el 
    resultado de la potencia usando sumas. 
    No se puede utilizar el operador de potencia.
'''
# Coloque la resolución del Ejercicio 3 debajo de esta línea

base = float(input("Ingrese la base: "))
exponent = int(input("Ingrese el exponente: "))

operation = 1

for value in range(1, (exponent + 1)):
      operation = round(operation * base)

print("Resultado de la potencia:",operation)

'''
    -----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Escriba un programa que genere una multiplicación de dos números 
    del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado 
    la respuesta correcta. Al inicio debe preguntar cuantas multiplicaciones 
    se van a hacer.
    El programa debe llevar la cuenta de las respuestas correctas e incorrectas 
    e indicar la nota correspondiente. 
        Si la nota es igual o mayor que 9, el programa felicitará al usuario por el resultado.
        Si se acierta la respuesta, se contabilizará como 1
        Si se acerca menos del 10% a la respuesta correcta, se contabilizará como 0.66.
        Si se acerca entre el 10% y el 30% a la respuesta correcta, se contabilizará como 0.33.
        Si se aleja más del 30% de la respuesta correcta, se contabilizará como 0.


'''
# Coloque la resolución del Ejercicio 4 debajo de esta línea

from random import randint

question = int(input("¿Cuantas multiplicaciones desea a realizar?\n>"))

correct_answers = 0
wrong_answers = 0
count = 0

while count < question:
  number1 = randint(2,10)
  number2 = randint(2,10)
 
  multiplication = number1 * number2

  question2 = int(input(f"¿Cuanto es {number1} * {number2}?\n>"))

  if question2 == multiplication:
    print('Respuesta correcta.')
    correct_answers+= 1
  else:
    print('Respuesta incorrecta.')
    wrong_answers += 1
  count += 1

print('-------------')
print(f"Respuestas correctas:  {correct_answers}")
print(f"Respuestas incorrectas: {wrong_answers}")
