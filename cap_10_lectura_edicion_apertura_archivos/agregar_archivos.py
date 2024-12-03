'''

EL METODO 'w' y 'r+' LO QUE HACEN ES SOBREESCRIBIR LO QUE HAY EN EL ARCHIVO DE TEXTO
SIN EMBARGO PODEMOS TAN SOLO AÑADIR INFORMACION EN LUGAR DE REEMPLAZAR LA ORIGINAL

PARA ELLO HACEMOS USO DE APPEND = 'a'

'''


ruta_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/mensaje_3.txt"

with open (ruta_archivo, 'a') as file_object:

     file_object.write ("\nEsta linea viene de Python")
     file_object.write('\n\tEsta otra linea tambien proviene de Python')