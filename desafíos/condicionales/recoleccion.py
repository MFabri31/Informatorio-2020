"""
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

    -La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M 
    -los barrios no céntricos con nombre posterior a la M. 
    -la sección B el resto.

Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.

"""


print("Indique el nombre del barrio y su ubicación.")

neighborhood_name = input("Nombre: ")
neighborhood_location = input("Ubicación:\na) Céntrico\nb) No céntrico.\n>")

neighborhood_location = neighborhood_location.lower()


if neighborhood_location != "a" and neighborhood_location != "b":
    print('Has ingresado el nombre o la ubicación de forma incorrecta, vuelva a intentarlo.')

if neighborhood_name < "m" and neighborhood_location == "a":
    print("El barrio",neighborhood_name,"se encuentra en la sección A")
elif neighborhood_name > "m" and neighborhood_location == "b":
    print("El barrio",neighborhood_name,"se encuentra en la sección A.")
else:
    print("El barrio",neighborhood_name,"se encuentra en la sección B")
