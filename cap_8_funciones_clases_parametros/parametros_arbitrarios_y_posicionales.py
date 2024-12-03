#PODEMOS TRABAJAR CON LA VARIEDAD DE PARAMETROS QUE HEMOS VISTO...

#ES DECIR, EN UNA FUNCION, UTILIZAR PARAMETROS POSICIONALES Y DESPUES ARBITRARIOS

def agregar_toppings_pizza(tamano, *toppings):

    print ("Haciendo pizza de medida: " + str(tamano) + '-pulgadas' + ' con los siguientes toppings: ')

    for topping in toppings:

        print ("Agregando: -" + topping)

agregar_toppings_pizza(16, 'jamon', 'salsa especial', 'orilla rellena de queso')
