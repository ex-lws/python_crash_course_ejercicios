#Los parametros de la funcion son las variables a usar y deben de colocarse respetando el orden en su 
#llamada posterior, es decir en su instanciación

def informacion_mascota(tipo_mascota, nombre_mascota):
	
	desplegar_informacion = "Mi mascota es un:" + " " + tipo_mascota.title() + " " + "y su nombre es:" + " " + nombre_mascota.title()
	
	print (desplegar_informacion)
	
informacion_mascota("perro", "dogen")
informacion_mascota("perro", "nalish")
informacion_mascota("gato", "tyna")

#Podemos modificar dichos parametros y la acción será la misma con ellos.

#Respetar el orden significa que...

informacion_mascota("vogen", "tortuga") #Vemos que se imprime mal enunciado por el mal orden de los parametros
