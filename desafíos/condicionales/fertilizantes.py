"""
Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la utilización de fertilizantes.


"""

compound = int(input("Porcentaje del compuesto: "))
type_of_vegetation = input("a) Vegetación normal\nb) Vegetación de tipo matorral.\n>")


if compound >= 10 and type_of_vegetation == "a":
    print('Es factible la utilización de fertilizantes.')
elif compound >= 10 and type_of_vegetation == "b":
    print('No es posible la utilización de fertilizantes.')
elif compound <= 10 and type_of_vegetation == "a" or type_of_vegetation == "b":
    print('No es posible la utilización de fertilizantes.')
else:
    print('Valor incorrecto. Vuelva a intentarlo.')
