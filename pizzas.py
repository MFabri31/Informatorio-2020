"""
Ejercicio 5: Nivel Difícil 

La pizzeria Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a contianuación.
Ingredientes vegetarianos: Pimiento y Rúcula
Ingredientes no vegetarianos: Jamón y Panceta

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

"""

welcomeMessage = "Hola bienvenidos a pizzeria Bella Napoli. Tenemos pizzas vegeterianas y no vegetarianas para ofrecerte."
warnMessage = "Ha ingresado valores incorrectos. intente nuevamente."
menu = "A continuación elija la pizza que usted desea. a) Pizza vegetariana b) Pizza no vegetariana."

print(welcomeMessage)
menu = input(menu)
 
if menu != "a" and menu != "b":
    print(warnMessage)


if menu == "a":
    ingredients = input("Por favor elija sus ingredientes. a) Pimiento  b) Rúcula.")
    if ingredients != "a" and ingredients != "b":
        print(warnMessage)
    if ingredients == "a":
        print("Ha elejido una pizza vegetarina con los siguientes ingredientes: mozzarella, tomate y pimiento.")
    elif ingredients == "b":
        print("Ha elejido una pizza vegetarina con los siguientes ingredientes: mozzarella, tomate y rúcula.")

if menu == "b":
    ingredients = input("Por favor elija sus ingredientes. a) Jamón  b) Panceta.")
    if ingredients != "a" and ingredients != "b":
        print(warnMessage)
    if ingredients == "a":
        print("Ha elejido una pizza no vegetarina con los siguientes ingredientes: mozzarella, tomate y jamón.")
    elif ingredients == "b":
        print("Ha elejido una pizza no vegetarina con los siguientes ingredientes: mozzarella, tomate y panceta.")
        