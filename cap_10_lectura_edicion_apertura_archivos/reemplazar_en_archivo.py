'''

el metodo replace('valor_original', 'valor_nuevo')

Reemplaza las palabras del archivo que encuentre y correspondan

'''

ruta_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/mensaje.txt"

with open (ruta_archivo) as file_object:

     contenido = file_object.read()

     contenido_modificado = contenido.replace('mago', 'malandro')

     print (contenido)
     print (contenido_modificado)

