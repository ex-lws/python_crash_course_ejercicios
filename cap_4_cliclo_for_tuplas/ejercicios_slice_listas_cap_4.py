lista_alumnos = ['Juan', 'Andres', 'Jhon', 'Devian', 'Eric']

#Imprimir slices.

print ('Los tres primeros elementos de lista son: ', lista_alumnos[0:3])
print ('Los tres elementos que componen la mitad de la lista son: ' , lista_alumnos[1:4])
print ('Los ultimos tres elementos de la lista son: ', lista_alumnos[2:5])

sabores_pizzas = ['hawaiana', 'peperoni', 'mexicana', 'queso', 'napolitana']

print ('Algunso sabors de pizza son: ' , sabores_pizzas)

#Copiar mediante slices.

sabores_favoritos_pizza = sabores_pizzas [:] #Hago una copia de la lista original

sabores_pizzas.append ('Bolognesa')

sabores_favoritos_pizza.append ('Margarita')

for pizza in sabores_favoritos_pizza:
    print (pizza)

for pizza in sabores_pizzas:
    print (pizza)

