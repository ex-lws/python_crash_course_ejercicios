#SANDWICHES

#AL TENER **POR LO TANTO SE TRATA DE UN PARAMETRO QUE PUEDE ALMACENAR MÁS PARAMETROS....
#ES DECIR UN PARAMETRO ARBITRARIO.

def hacer_sandwich(*ingredientes):

    for ingrediente in ingredientes:

        print ('Agregando ingrediente: ' + ingrediente.upper())

    print ('Sandwich con: ' + str(ingredientes))

sandwich_1 = hacer_sandwich('Jamon', 'lechuga', 'toamte cherry', 'mayonesa')
print (sandwich_1)

#USUARIOS

def agregar_info_usuario(nombres, apellidos, **info_extra):
    """METODO QUE AGREGA INFORMACION AL DICCIONARIO SOBRE EL USUARIO"""
    
    persona = {}
    persona['nombres_persona'] = nombres
    persona['apellidos_persona'] = apellidos

    for key, value in info_extra.items():

        persona[key] = value
        return persona

yo_como_usuario = agregar_info_usuario('Luis Alberto', 'Reyes Cruz', ciudad = 'ixtapaluca', edad = 19, nacionalidad = 'mexicana')
usuario_2 = agregar_info_usuario('Fernando Ixchel', 'Medina Reyes', localidad = 'Xochimilco', edad = 17, nacionalidad = 'ecuatoriana')

print (yo_como_usuario)
print (usuario_2)

#AUTOS

def agregar_auto (fabricante, modelo, **info_extra_auto):

    info_auto = {'Fabricante' : fabricante,
                 'Modelo' : modelo,
                 }
    
    for key, value in info_extra_auto.items():

        info_auto[key] = value
        return info_auto
    
    print (info_auto)
    
auto1 = agregar_auto('Ferrari', 'F40', caballos = '350', color = 'rojo')
print (auto1)

