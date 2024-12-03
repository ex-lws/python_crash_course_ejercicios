#Podemos acortar el codigo de meter dentro de una lista los valores de un for usando 
#list comprehension.

#Una list comprehension guarda los valores que genera el for en una lista que va asignada a 
#una variable.

#Tabla del 2, los valores que genera el for van a una variable

#El contenido de la lista es lo que hara el for, dentro de un rango del 0 al 10

lista_valores = [valor * 2 for valor in range (0, 11)] #A cada valor * 2, agregalo a la lista en un rango de 0 a 10

print (lista_valores)   

#Basicamente es una lista donde usamos ciclo for y alguna operaciones a la variable temportal...
