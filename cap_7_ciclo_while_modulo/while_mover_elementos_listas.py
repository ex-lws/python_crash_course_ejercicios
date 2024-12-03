#Podemos realizar bucles while en una lista de elementos.

#Mover elementos de una lista a otra mediante while loop.

#Recordemos que las listas sí permiten modificarse.


usuarios_no_verificados = ["Jean Baptiste", "Antoine Roquentin", "Arthur Meursault"] #Declaro una lista de elementos que moveré

usuarios_verficiados = [] #Una lista vacia, en la que añandiré elementos de la lista original.

while usuarios_no_verificados: #mientras existan elementos en la lista original...

  print ("Verificando usuarios.")
  usuario_actual = usuarios_no_verificados.pop() #Elimina el último elemento y lo manda a usuario actual

  usuarios_verficiados.append(usuario_actual)
  print ("Lista de usuarios verificados completada.") #Mete el contenido de usuario actual a usuarios verificados, la nueva lista.

for usuario in usuarios_verficiados: #Imprimo los elementos de la nueva lista.
  print (usuario)