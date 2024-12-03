ruta_archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/respuestas_usuarios.txt"


activador = True 
respuestas_usuarios = []

while activador:

     instrucciones = "Por favor escriba sus razones para programar..."

     respuesta_usuario = input (instrucciones)

     seguir = input("¿Quiere seguir agregando respuestas?...s/n")

     if seguir == 'n':
          
          print ("Respuestas almacenadas")
          respuestas_usuarios.append(respuesta_usuario.upper())
          activador = False

with open (ruta_archivo, 'a') as file_object:

     for respuesta in respuestas_usuarios:

          file_object.write ("\n" + respuesta)
