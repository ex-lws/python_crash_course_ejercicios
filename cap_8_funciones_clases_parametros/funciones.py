#Una función es un bloque de código que hace algo y requiere o no de parametros.
#Una funcion o metodo es una accion.


def imprimirMensaje ():

	'''METODO QUE IMPRIME UN MENSAJE'''
	
	print ("Hola a todos desde una función")
	
imprimirMensaje()

#Podemos llamar a la función en el momento más adecuado, con los parametros que necesitemos.

#UNA FUNCIÓN ES UNA ACCIÓN EN EL PROGRAMA QUE PUEDE TOMAR MUCHOS VALORES O PARAMETROS.

#Los parametros van dentro del parentesis, y lo que hay dentro es con lo que va a trabajar el metodo

def nombreUsuarioMayusculas(nombreUsuario):

	'''FUNCION QUE FORMATEA EL NOMBRE DE UNA PERSONA'''
	
	nombre_formateado = nombreUsuario.title()
	
	print (nombre_formateado)
	
nombreUsuarioMayusculas("luis reyes")
nombreUsuarioMayusculas("ximena vazquez")
nombreUsuarioMayusculas("octavio paz")

#POR CONVENCION, SE COLOCA JUSTO ARRIBA DE LO QUE HACE EL METODO CUAL ES SU PROPOSITO O FUNCION.