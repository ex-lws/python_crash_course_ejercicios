#Los promts son aquellas instrucciones que el usuario debe de seguir antes de escribir en consola

#Podemos mandar ese prompt a una variable y agregar tantas como queramos.


'''

variable = input(PROMPT O INSTRUCCIONES PARA EL USUARIO)

'''

instruccion = 'Hola, es un gusto verte de nuevo'
instruccion += '\nPor favor escribe tu nombre.'

nombre = input(instruccion)

print ('Bienvenido de nuevo: ' + nombre)