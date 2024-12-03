#Un diccionario puede almacenar listas dentro de las cuales almacenar elementos

#LISTA = []
#TUPLA = ()
#DICCIONARIO = {}

caracteristicas_pizza = {'masa' : ['delgada', 'especial', 'deep dish', 'rellena de queso', 'vegana'],
                         'toppings': ['peperoni', 'jamon', 'salami', 'anchoas', 'queso'],
                         'precio' : 250
                         }

print ('diccionario con todos los elementos de la pizza: ', (caracteristicas_pizza))

#Las keys toppings y masa son dos listas.

print ('Masas disponibles:', caracteristicas_pizza['masa'])
print ('Toppings disponibles:', caracteristicas_pizza['toppings'])