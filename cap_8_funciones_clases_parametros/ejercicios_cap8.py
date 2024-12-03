#REALIZAR PLAYERAS

def hacer_playera (talla, mensaje_estampado):

    mensaje_playera__realizada = "Su playera ha sido terminada con exito, la talla es:" + " " + talla.upper() + ', ' + 'el mensaje personalizado es:' + " " + mensaje_estampado

    print (mensaje_playera__realizada)

#LLAMAR LA FUNCION CON PARAMETROS DIRECTOS

hacer_playera ('m', 'Aprendiendo Python.')

#LLAMAR A LA FUNCION CON KEYWORD ARGUMENTS

hacer_playera(talla = 's', mensaje_estampado = 'Aprendiendo funciones con Python')

#REALIZAR PLAYERS CON PARAMETROS POR DEFAULT
#ES DECIR SI NO SE HACE UNA INSTANCIA DEL PARAMETRO SE TOMA POR DEFECTO I LOVE PYTHON!  

def realizar_playeras(talla_playera, mensaje_personalizado = 'I love Python!'):

    mensaje = 'Playera talla: ' + talla_playera + ' con mensaje: ' + mensaje_personalizado
    print(mensaje)

realizar_playeras(talla_playera='S')
realizar_playeras(talla_playera='M')
realizar_playeras(talla_playera='L')

#CAMBIAR EL VALOR POR DEFAULT EN LA LLAMADA

realizar_playeras('S', mensaje_personalizado ='I love Java')

#CIUDADES CON PAIES CON VALOR POR DEFECTO

def asignar_ciudades (ciudad, pais = 'mexico'):

    mensaje_ciudad = 'La ciudad de: ' + ciudad.title() + ' esta en: ' + pais.title()
    print (mensaje_ciudad)

asignar_ciudades('ciudad de mexico')
asignar_ciudades('guadalajara')
asignar_ciudades('monterrey')

#PG 174