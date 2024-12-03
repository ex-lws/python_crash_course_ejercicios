#EN UN DICCINARIO PODEMOS AGREGAR UN NUMERO INDETERMINADO DE ELEMENTOS

'''

Para esto se hace uso de los argumentos arbitrarios.
Estos puede almacenar más parametros instanciados.


**info extra almacenará dentro del diccionario los key y values que queramos...

'''

def agregar_info_usuario(nombres, apellidos, **info_extra):

    """METODO QUE AGREGA INFORMACION AL DICCIONARIO SOBRE EL USUARIO"""
    
    persona = {}
    persona['nombres_persona'] = nombres
    persona['apellidos_persona'] = apellidos

    #Agregamos los parametros al diccionario mediante un for

    for key, value in info_extra.items():

        persona[key] = value
        return persona
    
'''

Localidad y universidad son parte de los argumentos arbitrarios.

'''

usuario1 = agregar_info_usuario('Luis Alberto', 'Reyes Cruz', localidad = 'ixtapaluca', unviersidad = 'uaemex')

print (usuario1)