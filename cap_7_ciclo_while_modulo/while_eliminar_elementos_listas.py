#Podemos elimianar más de un elemento en una lista en caso de que sea necesario con un while.
#Para ello recordaremos el metodo de remove ("valor a borrar de la lista")

lista_usuarios = ["Reverendo Reyndolds", "Alfred Hithcok", "Ignis Hupert", "Delaware Soda", "Infracturs Devon", "Delaware Soda"]

print ("Lista original" , lista_usuarios)

#Ahora hacemos uso del while para elimianar elementos repetidos

while "Delaware Soda" in lista_usuarios: #Mientras exista delaware soda en la lista...
  lista_usuarios.remove("Delaware Soda") #Borra ese elemento de la lista y deten el bucle hasta que no quede ni uno.

print ("Lista tras borrar elementos repetidos. ",lista_usuarios)