'''

metodo que formatea datos sobre un pais y ciudad

'''

def formatear_ciudad(ciuad, pais, poblacion = ''):

     ciudad_formateada = 'ciudad' + ',' + '' + 'pais' + ',' + '' + 'poblacion: ' + str(poblacion) + '.'

     return ciudad_formateada.title()

formatear_ciudad ('ciudad de mexico', 'mexico')