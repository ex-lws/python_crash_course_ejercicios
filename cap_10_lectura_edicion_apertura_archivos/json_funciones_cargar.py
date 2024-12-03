import json 

ruta_archivo_json = '/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/numero_usuario.json'

with open (ruta_archivo_json, 'r') as file_object:

     numero_usuario = json.load(file_object)
     print ('Se que tu numero favorito es el :' + numero_usuario)