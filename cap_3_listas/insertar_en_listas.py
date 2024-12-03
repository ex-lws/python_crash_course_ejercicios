#Insertando elementos con un indice personalizado

#Para poder insertar utilizamos el metodo = nombreLista.insert(INDICE, CONTENIDO)

edades_estudiantes = [28, 18, 19, 21, 32, 20] #lista de nuemeros enteros

print (edades_estudiantes)

edades_estudiantes.insert(0, 17) #usamos insert(0, 17) para poder agregar al inicio de la lista el valor 17

print (edades_estudiantes)

lista_empleados = ["Angel", "Charles", "Gabriela"] #Lista, pero con valores strings

print (lista_empleados)

#Insertamos, pero con otros indices, es decir otros lugares de la lista

lista_empleados.insert (-3, "Juan")
lista_empleados.insert(0, "Karla")
lista_empleados.insert(-2, "Hipolito")

print (lista_empleados)

#Recoordemos que tambien se pueden añadir elementos usando append
#Append solo necesita el valor que ira a la ultima parte de la lista
#Insert requiere del indice y el valor a agregar, es dedcir, esos son sus parametros

lista_ejemplo = ["Mauricio", "Juan Carlos"]

print (lista_ejemplo)

lista_ejemplo.append('Charles') #append siempre agrega elementos al final de la lista


print (lista_ejemplo)

#INSERT REQUIERE DEL VALOR DEL INDICE Y EL CONTENIDO PARA AGREGAR A LA LISTA

#nombreLista.isnert(indice, "valor")

#APPEND SOLO REQUIERE DEL CONTENIDO PARA AGREGAR A LA LISTA Y LO MANDA AL ULTIMO LUGAGR SIEMPRE 

#nombreLista.append("valor")
