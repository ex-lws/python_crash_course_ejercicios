'''

Una vez que hemos dumpeado la informacion del JSON, lo que toca ahora es cargar dicha informacion, pero en otro programa...

'''


#Importamos la libreria de JSON

import json

#COLOCAMOS LA RUTA DEL ARCHIVO JSON EN UNA VARIABLE

nombre_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/sueldos.json"

#LEEMOS EL ARCHIVO

with open (nombre_archivo, 'r') as file_object:

     #MANDAMOS EL CONTENIDO DEL ARCHIVO JSON O EL LOAD DEL JSON A UNA VARIABLE PARA DESPUES IMPRIMIRLA EN CONSOLA

     cotenido = json.load(file_object)
     print (cotenido)

     