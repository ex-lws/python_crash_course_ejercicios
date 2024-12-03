#LAS FUNCIONES PUEDEN INSTANCIARSE EN CUALQUIER MOMENTO

#PUEDEN LLEVAR ALGO LLAMADO KEYWORD ARGUMENTS, QUE ES EXACTAMENTE EL MISMO PARAMETRO DENTRO DE LA LLAMADA.

'''

EJEMPLO = def metodoSuma (valor1, valor2)

INSTANCIA DEL EJEMPLO CON KEYWORD ARGUMENTS

SE COLOCA EL NOMBRE DEL PARAMETRO

metodoSuma (valor1 = 2, valor2 = 7)

INSTANCIA DEL PARAMETRO SIN KEYWORD ARGUMENTS

metodoSuma(2, 7)



'''
def imprimirNombreMascota(nombre_mascota, tipo_mascota, edad_mascota):
	
	
	info_mascota = "Su mascota es:" + " " + nombre_mascota.title() + " " + "y es de tipo:" + " " + tipo_mascota.title() + " " + "y tiene:" + " " + str(edad_mascota) + " " + "años." 
	
	print (info_mascota)
	
#INSTANCIAR LA FUNCION CON KEYWORD ARGUMENTS (RECOMENDABLE)


imprimirNombreMascota(nombre_mascota ="lazarus", tipo_mascota = "pescado dorado", edad_mascota = 2)
