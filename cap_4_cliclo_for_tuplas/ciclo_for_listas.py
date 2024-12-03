#El ciclo for permite realizar una tarea n veces.

lista_magos = ['oz', 'chris', 'spelunky'] #Definimos una lista con varios elementos dentro, 
#en este caso 3, por lo tanto el for iterará 3 veces, una por cada elemento de la lista.

print (lista_magos)#Impirmir el contenido de la lista.
print (len(lista_magos)) #Impirmir la cantidad de elementos de la lista.

for mago in lista_magos: #Esta es la sintaxtis del for, para cada variable temporal mago 
	#dentro de la lista magos, haz esto...
    print ('Bienvenido: ' + mago.title()) #Damos un tab para indicar que las instrucciones a iterar estan 
    #dentro del for

print ('Fin del bucle.') #Esto ya no es parte del bucle

lista_generica = [2, 2] #Colocamos 2 valores, cada uno pasara a la viriable temporal numero

for numero in lista_generica:

    print (numero + 5) #Cada valor de la lista se sumara en el loop, tantas veces se tengan elementos en la 
    #lista, sería sumar 2 + 5 y 2 +5...
    print ('Sumando...')

#Por convecion, la variable temporal tiene el nombre en singular de los elementos que conforman la lista

