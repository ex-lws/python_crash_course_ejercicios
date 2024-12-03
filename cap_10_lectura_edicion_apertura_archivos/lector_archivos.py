'''

ESTE ES UN PROGRAMA QUE LEE UN ARCHIVO E IMPRIME EN CONSOLA SU CONTENDIO

'''


#LA FUNCION with open (REQUIERE DE QUE EL ARCHIVO ESTÉ EN LA CARPETA DEL PROGRAMA)
#EL ARCHIVO SE VA A LA VARIABLE file_object:


#RUTA ARCHIVO ES UNA VARIABLE QUE ALMACENA LA DIRECCION DE NUESTRO ARCHIVO A LEER


ruta_archivo = '/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/digitos_pi.txt'

with open (ruta_archivo) as file_object:

     #file_object.read() es un metodo para leer el archivo.

     contenido = file_object.read()
     print (contenido)

     