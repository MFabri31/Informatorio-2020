"""
Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la utilización de fertilizantes.


"""
welcomeMessage = "Necesitamos que indique un porcentaje del compuesto que utiliza y si la vegetación es de tipo matorral."
successMessage = "Es factible la utilización de fertilizantes."
warnMessage = "No es posible la utilización de fertilizantes."
errorMessage = "Has introducido un valor incorrecto por favor vuelva a intentarlo."


print(welcomeMessage)

compound = int(input("Porcentaje del compuesto: "))
typeOfVegetation = input("a) Vegetación normal b) Vegetación de tipo matorral.") 

if compound >= 10 and typeOfVegetation == "a":
    print(successMessage)
elif compound >= 10 and typeOfVegetation == "b":
    print(warnMessage)
elif compound <= 10 and typeOfVegetation == "a" or typeOfVegetation == "b":
    print(warnMessage)
else:
    print(errorMessage)