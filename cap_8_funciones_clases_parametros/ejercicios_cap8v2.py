#CIUDAD

#VALOR POR DEFECTO QUE ES CHILE POR LO QUE NO ES NECESARIO INSTACIARLO

def imprimirCiudad (nombre_ciudad, pais = 'Chile'):

    mensaje = 'La ciudad de: ' + nombre_ciudad + ', se encuentra en: ' + pais
    return mensaje.title()

primer_ciudad = imprimirCiudad('santiago')
segunda_ciudad = imprimirCiudad('ciudad de mexico', 'mexico')
tercera_ciudad = imprimirCiudad('new york', 'estados unidos')

print (primer_ciudad)
print (segunda_ciudad)
print (tercera_ciudad)

#HACER ALBUM Y ALMACENAR DATOS EN UN DICCIONARIO Y CON PARAMETROS OPCIONALES.
#NUMERO DE CANCIONES ES UN PARAMETRO OPCIONAL POR LO TANTO SE PUEDE EVITAR SU INSTANCIACION.


def almacenarAlbum (nombre_disco, autor, numero_canciones = ''):

    if numero_canciones:

        almacen_discos = {'nombre_disco': nombre_disco.title(), 'autor_banda': autor.title(), 'total_canciones': numero_canciones}
        return almacen_discos
    
    else:
        almacen_discos = {'nombre_disco': nombre_disco.title(), 'autor_banda': autor.title()}
        return almacen_discos
    
disco_1 = almacenarAlbum('antics', 'interpol')
print (disco_1)
disco_2 = almacenarAlbum('dark side of the moon', 'pink floyd', 24)
print (disco_2)

while True:

    print ('Bienvenido al programa de creacion de discos personalizado')
    nombre_disco_personalizado = input ('Escriba el nombre del disco.')
    autor_disco_personalizado = input ('Escriba el autor o banda del disco.')

    agregar_nuevo = input ('Desea agregar otro disco s/n')

    if agregar_nuevo == 's':
        print ('Disco agregado con exito.')
        autor_disco_personalizado = almacenarAlbum(nombre_disco_personalizado, autor_disco_personalizado)
        print (autor_disco_personalizado)
    
    else:
        print ('Cerrando programa...')
        break
    
    




