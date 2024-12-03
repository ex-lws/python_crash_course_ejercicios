toppings_pizza = []

#toppngs disponibles

toppings_pizza.append('peperoni')
toppings_pizza.append('anchoas')
toppings_pizza.append('jamon')
toppings_pizza.append('salchicha')

for topping in toppings_pizza:

    #Ya no hay jamon

    if topping == 'jamon': #Si en la lista aparece jamon...
        print ('Ya no tenemos jamon, seleccione otro topping diferente.')

    else:
        print ('Seleccionado toppings: ' , topping.title()) #Continua la seleccion

print ('\n\tPizza preparada')