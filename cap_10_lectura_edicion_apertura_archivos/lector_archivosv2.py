'''

ESTE PROGRAMA LEE EL CONTENIDO DEL ARCHIVO Y MEDIANTE UN FOR LOOP IMPRIME SU CONTENIDO LINEA POR LINEA

'''


ruta_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/breve_reflexion.txt"

#RUTA ARCHIVO ES FACILMENTE NUESTRO ARCHIVO


with open (ruta_archivo) as file_object:

     #POR CADA LINEA EN EL ARCHIVO, IMRPRIMELA.
     
     for line in file_object:
          print (line)
