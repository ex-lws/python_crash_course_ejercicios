#Podemos cambiar los valores del diccionario simplemente renombrando el valor de 
#la llave.

'''

Sintaxis 

nombreDiccionario["key"] = nuevoValue

'''

caracteristicas_escuela = {'numero de salones' : 25, 
                           'carreras impartidas': 6, 
                           'nombre de la universidad' : 'Abism'}

print (caracteristicas_escuela)

#Cambiar el valor del numero de los salones a 23

caracteristicas_escuela['numero de salones'] = 23
caracteristicas_escuela['carrera impartidas'] = 10

#Agrego un nuevo elemento al diccionario

caracteristicas_escuela['Periodos vacacionales al año'] = 2
print (caracteristicas_escuela)
 
print ('Nuevo diccionario con el numero de salones actualizado.', caracteristicas_escuela)