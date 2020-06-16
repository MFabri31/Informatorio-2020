"""
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

    -La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M 
    -los barrios no céntricos con nombre posterior a la M. 
    -la sección B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.

"""

warnMessage = "Has ingresado el nombre o la ubicación de forma incorrecta, vuelva a intentarlo."

print("A continuación indique el nombre del barrio y su ubicación.")

neighborhoodName = input("Nombre: ")
neighborhoodLocation = input("Ubicación: a) Céntrico b) No céntrico. ")

neighborhoodLocation = neighborhoodLocation.lower()


if neighborhoodLocation != "a" and neighborhoodLocation != "b":
    print(warnMessage)

if neighborhoodName < "m" and neighborhoodLocation == "a":
    print("El barrio",neighborhoodName,"se encuentra en la sección A")
elif neighborhoodName > "m" and neighborhoodLocation == "b":
    print("El barrio",neighborhoodName,"se encuentra en la sección A.")
else:
    print("El barrio",neighborhoodName,"se encuentra en la sección B")
