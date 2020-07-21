"""
Ejercicio 3: Nivel Fácil
 
Se necesita calcular el resultado final de un cuestionario realizado por una persona.
Solicita cantidad total de preguntas y luego cantidad de respuestas correctas
-Si el porcentaje de respuestas correcta es mayor o igual a 90 ek resultado es EXCELENTE
-Si el porcentaje de respuestas correcta es mayor o igual a 70, el resultado es BUENO
-Si el porcentaje de respuestas correcta es mayor o igual a 60, el resultado es APROBADO
-Si el porcentaje de respuestas correcta es menor a 60, el resultado es No alcanzó

"""

question = int(input("Ingrese el todal de preguntas realizadas: "))
correct_answers = int(input("Indique la cantidad de preguntas correctas: "))
percentage = (correct_answers * 100) / question


if percentage >= 90:
    print("Resultado: Excelente")
elif percentage >= 70:
    print("Resultado: Bueno")
elif percentage >= 60:
    print("Resultado: Aprobado")
else:
    print("No alcanzó")
