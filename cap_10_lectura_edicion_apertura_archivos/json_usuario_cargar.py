'''
Importaremos la informacion de otro programa aqui

'''

import json 

datos = '/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/datos_usuario.json'

with open (datos, 'r') as file_object:

     nombre_usuario = json.load(file_object)
     print ('Bienvenido: ' + nombre_usuario)