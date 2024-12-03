#Podemos creear un diccionario dentro de un diccionario.

#En este caso tenemos dos diccionarios diferententes dentro del mismo diccionario.

#El diccionario usuarios...

usuarios = {
    
	'devon777' : {
        

	   'nombres' : 'luis alberto',
        'apellidos' : 'reyes cruz',
        'edad' : 23,
        'ciudad' : 'baja california'
        


	},
    
	'enrich01' : {
        
	   'nombres' : 'ximena regina',
        'apellidos' : 'vazquez landeros',
        'edad' : 19,
        'ciudad' : 'fresno'

	}



}

print (usuarios)

#Recordemos que key, en este caso sera el username, y los value aquello albergado 
#en username.

for key, value in usuarios.items(): #key = atriburo. value = contenido del atributo
    
	print ('Nombre de usuario: registrado en el sistema: ' + key.upper())
	print ('Datos registrados del usuario en el sistema: ' + '\n' + '\t' + str(value))
	nombre_completo = value['nombres'] + value ['apellidos']

	print (nombre_completo)



						
