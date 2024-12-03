'''

podemos agregar nuevos elementos a un diccionario mediante la sintaxis = 

nombreDiccionario['key'] = valor

'''

caractesiticas_empresa = {'empleados' : 5, 
                          'vigilantes' : 2, 
                          'nombre_empresa' : 'ancient memories'}

print (caractesiticas_empresa)

#Para agregar nuevos valores a la cola del diccionario...
#Dentro del corchete el key. Después del igual el value.

caractesiticas_empresa['giro_empresa'] = 'software'
caractesiticas_empresa['valor estimado'] = 60000000

print (caractesiticas_empresa)

print (caractesiticas_empresa) #Imprimo todo lo que contiene el diccionario.

#Imprimo solo aquellos valores que me interesan, utilizando las keys.

print (caractesiticas_empresa['empleados'])
print (caractesiticas_empresa['vigilantes'])

#De igual manera puedo empezar con un diccionario vacio al cual le agregare 
#elementos mas tarde

carrera_f1 = {} #Diccionario sin elementos

#agregamos los elementos con sus llaves e informacion.
#Recordemos que cada elemento del diccionario se compone de key and value.

carrera_f1['equipos'] = 'ferrari', 'mclaren', 'mercedes', 'red bull', 'hass', 'alpine', 'sauber'
carrera_f1['pais oirginario'] = 'inglaterra'
carrera_f1['total de carreras en 2024'] = 24

print (carrera_f1)
