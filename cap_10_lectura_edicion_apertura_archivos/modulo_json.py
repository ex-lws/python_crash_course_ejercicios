'''

El modulo JSON permite guardar informacion contenida en estrcuturas de datos como lo pueden ser listas, tuplas y diccionarios...
Dicha informacion puede ser datos del usuario o del programa unicamente

'''

import json

lista_sueldos = [550, 1220, 910, 620, 515, 1700] #LISTA QUE CONTIENE LOS DATOS

#COLOCAMOS EL NOMBRE DEL ARCHIVO Y LA RUTA DONDE SE GUARDARA EL JSON CON LOS DATOS

nombre_archivo = '/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/sueldos.json'

with open (nombre_archivo, 'w') as file_object:

     json.dump(lista_sueldos, file_object) #json tiene varios modulos, entre ellos el dump, que guarda la informacion