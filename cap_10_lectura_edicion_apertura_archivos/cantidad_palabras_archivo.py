'''

ESTE PROGRAMA CUENTA LA CANTIDAD DE PALABRAS DE UN ARCHIVO

'''

ruta_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/dead_souls.txt"

with open (ruta_archivo, 'r') as file_object:

     contenido_libro = file_object.read()

     palabras = contenido_libro.split() #SEPARA EN PALABRAS TODO EL TEXTO

     total_palabras = len(palabras) #EN UNA VARIABLE NUEVA, CONTAMOS CUANTAS PALABRAS HAY EN TOTAL
     
     print ("Este libro: " + ruta_archivo + " tiene en total: " + str(total_palabras))