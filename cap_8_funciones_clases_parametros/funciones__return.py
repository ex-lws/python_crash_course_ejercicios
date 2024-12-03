#EL RETURN ES BASICAMENTE REGRESAR LA OPERACION DE LOS PARAMETROS

def sumar (valor1, valor2):

    suma = valor1 + valor2
    return suma #REGRESA EL RESULTADO DE VALOR1 + VALOR2

#EL RESULTADO DEL METODO LO ALBERGAMOS EN UNA VARIABLE

resultado_suma = sumar(5, 75)
print(resultado_suma)

#RETURN ES BASICAMENTE EL RESULTADO DE OPERAR LOS PARAMETROS

def formatear_nombre (primer_nombre, apellidos):

    nombre_completo = primer_nombre + ' ' + apellidos
    return nombre_completo.title()

nombre_formateado = formatear_nombre('luis alebrto', 'reyes cruz')
print (nombre_formateado)