"""
Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

    -Ingredientes comunes: Verduras y berenjena.
    -Ingredientes Receta 1: Lentejas y apio.
    -Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.

"""

print("Elija el tipo de receta ecológica que desea.")

ingredients1 = ["lentejas","apio"]
ingredients2 = ["morrón","cebolla"]

question = input("a) Receta 1 b) Receta 2.")
question = question.lower()


if question != "a" and question != "b":
    print("Intente nuevamente a ingresado un valor incorrecto.")   
         

if question == "a":
    ingredients = input("Por favor indique los ingredientes. a) Verduras b) Berenjenas.")

    if ingredients == "a":
        print("Usted a elejido la receta 1 con las siguientes ingredientes.")
        for i in ingredients1:
            print(i)
        print("verduras") 

    elif ingredients == "b":
        print("Usted a elejido la receta 1 con las siguientes ingredientes.")
        for i in ingredients1:
            print(i)
        print("berenjenas")    
         

if question == "b":
    ingredients = input("Por favor indique los ingredientes. a) Verduras b) Berenjenas.")

    if ingredients == "a":
        print("Usted a elejido la receta 2 con las siguientes ingredientes.")
        for i in ingredients2:
            print(i)
        print("verduras") 

    elif ingredients == "b":
        print("Usted a elejido la receta 2 con las siguientes ingredientes.")
        for i in ingredients2:
            print(i)
        print("berenjenas")

    