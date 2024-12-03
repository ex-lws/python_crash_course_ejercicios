'''

Podemos saber cuantas veces se repite una palabra en especifico en un texto

'''

ruta_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/palabras_repetidas.txt"

with open (ruta_archivo, 'r') as file_object:

     contenido = file_object.read()

     palabras_duplicadas = contenido.lower().count('mundo') #FORMATEO EL TEXTO A MINUSCULAS PARA ABARCAR TANTO MINUSCULAS COMO MAYUSCULAS.
     print (palabras_duplicadas)

