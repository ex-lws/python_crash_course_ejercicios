#añadir reemplazando elementos de las listas

marcas_ropa = ["zara", "polo", "gap"] #Definimos una lista con varios elementos

print (marcas_ropa) #Imprimimos el contenido de la lista

#Podemos cambiar los elementos o el contenido de un elemento de una lista simplemente sobreescribiendolo

#nombreLista[indice del elemento a reemplazar] = valor que sera el nuevo

marcas_ropa[0] = "american eagle"
marcas_ropa[1] = "nike"
marcas_ropa[2] = "vans of the wall"

print (marcas_ropa)

#Podemos añadir elementos con el metodo LISTA.append('elemento)

#Este no sobreescribe nada y lo agrega a la cola de la lista, la cola se puede agrandar tantos 
#append como queramos y la lista seguirá creciendo.

marcas_ropa.append ("bershka")
marcas_ropa.append ("northface")

print (marcas_ropa)#La lista crece...

#Podemos añadir elementos incluso a una lista vacia si asi se quiere

dulces = [] #lista vacia

#La añadimos elementos...

dulces.append ("cocada")
dulces.append ("tamarindo")
dulces.append ("paleta de nanches")

print (dulces)

print (dulces[-2].title())


