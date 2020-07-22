"""
1.En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra. 
Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 

Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento.

"""


while True:
    try:
        total_to_pay = int(input("Importe a pagar: \n>"))
    except ValueError:
        print('Debe ingresar un valor numérico.')
    else:
        break


while True:


    discount = input("Ingrese el descuento: A) Amarillo B) Blanco R) Rojo.").lower()


    while (discount != "a") and (discount != "b") and (discount != "r"):
        print("Por favor ingrese nuevamente el codigo.")
        discount = input("Ingrese el descuento: R) Rojo A) Amarillo  B) Blanco.")
    
    print('-----------------')
    
    if discount == "r":
        print("Descuento obtenido: 40%")
        total_to_pay = round(total_to_pay - (40 * total_to_pay) / 100)
    elif discount == "a":
        print("Descuento obtenido: 25%")
        total_to_pay = round(total_to_pay - (25 * total_to_pay) / 100)
    elif discount == "b":
        print("No tiene ningun tipo de descuento.")
            
    break


print(f'Importe total a pagar: ${total_to_pay}')
    
