'''

El modulo JSON puede guardar informacion sobre el usuario...

'''

import json 

datos_usuario = input('Por favor, escriba su nombre')

datos_usuario_json = '/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/datos_usuario.json'

with open (datos_usuario_json, 'w') as file_object:

     json.dump(datos_usuario, file_object)

     print ('Datos guardados externamente: ' + datos_usuario.title())