ruta_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/gatos.txt"
ruta_archivo_2 = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/perros.txt"
ruta_archivo_3 = "no existe"

archivos = []

archivos.append(ruta_archivo)
archivos.append(ruta_archivo_2)
archivos.append(ruta_archivo_3)

try:

     for archivo in archivos:

          with open (archivo, 'r')as file_object:

               contenido = file_object.read()

               print ("CONTENIDO DEL ARCHIVO:" + "\n" + contenido)

except FileNotFoundError:

     print ("Uno de los archivos no existe en la ubicación asignada.")
