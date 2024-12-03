ruta_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/aprendiendo_python.txt"

with open (ruta_archivo) as file_object:


     for archivo in range(0, 3):

          print ("***IMPRIMIENDO***")

          contenido = file_object.read()
          print (contenido)
