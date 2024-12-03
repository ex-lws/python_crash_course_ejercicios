#PROGRAMA QUE METE EN UN TXT EL NOMBRE DEL USUARIO

print ("***BIENVENIDO AL PROGRAMA")

instucciones = "Por favor, escriba su nombre de usuario:"

nombre_usuario = input(instucciones)

#EL ARCHIVO ORIGINAL SE LLAMA MENSAJE_4 Y TIENE COMO TEXTO NOMBRE_USUARIO

ruta_arhivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/mensaje_4.txt"

with open (ruta_arhivo, 'w') as file_object:

     file_object.write(nombre_usuario)