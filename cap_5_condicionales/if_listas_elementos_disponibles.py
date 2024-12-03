toppings_pizza_disponibles = ['peperoni', 'anchoas', 'carnes frias', 'chorizo', 'jamon', 'queso', 'champinon']

toppings_seleccionados = ['peperoni', 'champinon']

for toppings_seleccionados in toppings_seleccionados:

    if toppings_seleccionados in toppings_pizza_disponibles: #Compara los elementos de ambas listas.
        print ('Agregando topping: ', toppings_seleccionados.title())

    else: #si hay un topping no disponible...
        print ('Lo siento, su topping no esta disponible para agregar a su pizza.')

print ('Pizza completada.')

print ('Disfute su pizza')

