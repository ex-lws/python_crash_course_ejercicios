#LOS MODULOS EN PYTHON SON BASICAMENTE FUNCIONES O METODO ALMACENADOS DE MANERA INDEPENDIENTE 
#PARA PODER USARSE EN OTRAS CLASES O PRGRAMAS...

#AQUI ALMACENAMOS AGREGAR_PIZZA = METODO

def agregar_toppings_pizza(*toppings):

    '''Metodo que agrega toppings a una lista e imprime cada uno de ellos'''

    for topping in toppings:

        print ("Agregando: -" + topping)
        
    print ("Pizza finalizada con los siguietens ingredientes: " + str(toppings))

