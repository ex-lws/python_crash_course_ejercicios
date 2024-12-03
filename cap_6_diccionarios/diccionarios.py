#Un diccionario es un conjunto de informacion sobre algo

#Se abre con llaves, donde podemos colocar caracterisitcas, es decir atributos 
#con informacion dentro {ELEMENTOS}

#Cada atributo dentro del diccionario se le llama llave y su contenido value. KEY + VALUE

#Las llaves o atributos siempre van entre comillas simples, posteriormente : 
#y el valor a guardar, al estilo de MongoDB

#Si lleva String entonces poner entre comillas, si es numero no las necesita. (VALUES)

#El diccionario puede guardar numeros, strings, listas, tuplas y hasta otros 
#diccionarios.

#Cada elemento de un diccionario es un conjunto de key y value

alien = {'color': 'rojo', #PRIMER ELEMENTO
         'piernas': 2} #SEGUNDO ELEMENTO

print (alien) #Podemos imprimir todo lo que contiene el diccionario

#Podemos imprimir el contenido de lo que queremos dependiendo el atributo del diccionario mendante KEYS

print (alien['color'])
print (alien['piernas'])

print ('El alien es de color: ', alien['color'], ' y tiene el numero de piernas de: ',   
       alien['piernas'])
