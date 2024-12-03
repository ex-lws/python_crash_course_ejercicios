#podemos utilizar bucles para poder crear diccionarios.

#Genero una lista vacia en la cual voy a agregar varios elementos

diccionario = []

#Genero un bucle for en el que hara una iteracion 10 veces

for elemento in range (0, 10):
    nuevo_elemento = {'color' : 'rojo', 'nombre' : 'Manny'} #creara 10 veces este diccionario
    diccionario.append(nuevo_elemento) #mandara los 10 diccionarios a la lista

print (diccionario)

print (len(diccionario)) #veo la cantidad de elementos almacenados en la lista

#Podemos modificar los elementos que tengamos almacenados en la lista en caso de que lo queramos.

#Por ejemplo, supongamos que quiero modificar los primeros 5 elementos...

#Vamos a iterar en la lista y si en algun elemento del diccionario, del 0 al 3...
#Hay una key que tenga valor de rojo, entocnes para esos 3 cambia estos valores

for parte_diccionario in diccionario[0:3]: #recorro la lista
    print (parte_diccionario) #imprimo la lista para verificar el recorrido...

    if parte_diccionario['color'] == 'rojo': #si hay una key y un value de rojo, entonces para esos 3 elementos...  
        parte_diccionario['color'] = 'verde'
        parte_diccionario['nombre'] = 'anselmo'

    elif parte_diccionario['color'] == 'verde':
        parte_diccionario['color'] = 'morado'
        parte_diccionario['nombre'] = 'Ricardo'

print (diccionario)
