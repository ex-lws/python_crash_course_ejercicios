#orderna_listas_alfabeticamente

lista_alumnos = ['mariana itzel', 'luis alberto', 'angel gustavo']

#El metodo listaNombre.sort() lo que hace es ordenar alfabeticamente lo que hay en la lista y 
#cambiar el orden permanentemente

lista_alumnos.sort() #ordena alfabeticamente los elementos de la lista (PERMANENTE)

print (lista_alumnos)

#Podemos ordernar alfabeticamente al reves usando como parametro reverse = True dentro de sort()
#EL ORDEN CAMBIA PARA SIEMPRE

lista_autos = ['bmw', 'audi', 'mercedes']

lista_autos.sort(reverse = True) #Orden alfabetico, pero inverso.

print (lista_autos)

#Ambos metodos lo que hacen es ordenar la lista, sin embargo, ya no vuelve a su estado original o 
#su orden original
#Hacemos uso del metodo sorted dentro del print para poder cambiar el orden sin alterlarlo 
#permanentemente

#Mediante consola...
#print (sorted(lista a ordenar alfabeticamente))

lista_empleados = ['Coreline Manson', 'Adamaris Chavez', 'Ignacio Lopez']

#Hacemos uso del metodo sorted

print (sorted (lista_empleados)) #Va dentro del print y no altera el orden original de la lista

print (lista_empleados) #Orden original 

#.sort() cambia el orden de la lista a alfatecamente.

#print(sorted(nombre_lista)) no cambia el orden la lista de manera permanente, pero si muestra su orden unicamente
#alfabeticamente, ideal solo para consola.

