#podemos borrar elementos de una lista usando del, nombre lista e indice entre corchetes 
#para seleccionar el elemento a eliminar

#Recordemos que el indice siempe parte del 0...

#0,1,2,3

#Sintaxis = del nombreLista[indice]

#         0         1         2         3

lista = ["Perro", "gato", "Liebre", "Serpiente"]

print (lista)

del lista [0] #Perro borrado
del lista [2] #Liebre borrada

#del es mas espcifico, borra siguiendo el indice..

print (lista)

#podemos remover elementos usando pop
#pop elimina el útimo elemento de la lista.

#Sintaxis = nombreLista.pop()

lista_juegos = ["dirt rally", "dirt rally 2.0", "wrc", "f1 2024"]

print (lista_juegos) #lista origigal

#Podemos mandar el último elemento eliminado a una variable nueva

elemento_removido = lista_juegos.pop()

print (lista_juegos)

print (elemento_removido) #Ultimo elemento que borramos

#podemos quitar o remover elementos usando el metodo remove y entre paresentsis el valor
#Util para cuando no sabemos el valor del indice, pero si el contenido de lo que queremos corrar

#Sintaxis = nombreLista.remove("valorContenidoEnLista")

nombres_estudios = ['From Software', 'Imsomniac', 'Codemasters']

print (nombres_estudios)

nombres_estudios.remove("From Software")

print (nombres_estudios)

#Podemos incluso poder asignar a una variable lo que queremos borrar

lista_lentes = ["rayban", "ben and frank"]

print (lista_lentes)

quitar_marca = "ben and frank"

lista_lentes.remove(quitar_marca)

print (lista_lentes)

#En caso de ser números simplemente quitamos las comillas y colocamos el valor a borrar


lista_edades = [26, 15, 13, 21]

print (lista_edades)

lista_edades.remove(26) #removemos el valor 26
lista_edades.remove(21) #removemos el valor 21

print (lista_edades)

#del nombreLista[indiceElemento]

#listaElemento.pop() = Ultimo elemento agregado el que se borrará

#listaElemento.remove("elementoIntegroLista") = Borrando por el mismo elemento.

