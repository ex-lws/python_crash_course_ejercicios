#VALORES POR DEFECTO EN FUNCIONES

#PODEMOS ASIGNAR DESDE LA DECLARACIÓN DE LA FUNCIÓN UN PARAMETRO O ARGUMENTO POR DEFECTO QUE SE PUEDE OBVIAR
#UTIL EN CASO DE QUE SEA UNA CONSTANTE O UN VALOR REPETIVIVO


def agregarNuevoBibliotecario (nombre_bibliotecario, biblioteca = "Sor Juan Inés de la Cruz"):
	
	mensaje_bienvenida = "Bienvenido" + " " + nombre_bibliotecario.title() + " a: " + biblioteca + "."
	
	print (mensaje_bienvenida)
	
#AL SIEMPRE PERTENECER A LA BIBLIOTECA, ENTONCES NO HAY NECESIDAD DE INSTANCIARLO EN LA LLAMADA DE LA FUNCIÓN

agregarNuevoBibliotecario("braulio díaz")

#EN EL CASO DE LA TABLA DEL 5, EL 5 ES EL VALOR QUE SE REPITE HASTA EL 10, POR LO TANTO SE PONE POR DEFAULT


def tablaDel5 (valor1, valor2 = 5):
	
	resultado = valor1 * valor2
	print (resultado)
	
tablaDel5(3)
tablaDel5(9)
tablaDel5(10)
tablaDel5(22)
