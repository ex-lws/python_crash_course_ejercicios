#Podemos borrar los valores que hay en el diccioanrio mediante del nombre de la llave

'''

sintaxis

del nombreDiccionario["key"]

'''

caracterisitcas_libreria = {'cantidad de libros' : 2500, 'nombre libreria': 'Letras Libres', 'ubicacion' : 'Nueva Inglaterra'}

print (caracterisitcas_libreria)

#Para ello utilizamos el metodo del[key a borrar]
#Borrará tanto la key como el value en el diccionario.
#Requiere del elemento exacto de la key, es decir el nombre tal cual se asignó orignalmente en el diccionario.

del caracterisitcas_libreria['ubicacion']
del caracterisitcas_libreria["nombre libreria"]

print (caracterisitcas_libreria)