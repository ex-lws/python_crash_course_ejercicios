#Podemos realizar copias de nuestras listas indicando la cantidad de elementos que queremos copiar 
#y mandarla a una nueva variable

lista_comidas = ['pizza', 'pastel', 'ramen', 'sushi']

#Podemos imprimir o loopear en un rango de valores de la lista...

print (lista_comidas[1:4]) #Imprimo unicamente esos elementos selccionados mediante el indice.

#Para copiar todos los elementos de la lista [:]

comidas_amigo = lista_comidas[:] #Copiamos todos los elementos de la lista sin necesidade de colocar valores

print (comidas_amigo)

#Pasarle solo sushi y ramen otra variable

comidas_orientales = lista_comidas[2:4] #solo copiaré los elementos asiaticos para mandarlos a otra variable.

print (comidas_orientales)
