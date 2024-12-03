import json

def guardarNumeroUsuario():

     instrucciones = 'Bienvenido, por favor escriba su numero favorito...'

     numero_usuario = input(instrucciones)

     numero_usuario_json = '/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/numero_usuario.json'

     with open (numero_usuario_json, 'w') as file_object:

          json.dump(numero_usuario, file_object)
          print ('Datos guardados con exito')
     
guardarNumeroUsuario()