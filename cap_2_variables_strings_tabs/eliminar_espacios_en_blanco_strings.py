#Podemos borrar los espacios en blanco de los strings, en caso de ser necesario

#requiere del metodo strip; 
# rstrip para los espacios en la derecha. 
# lstrip para los espacios en la izquierda
# strip para espacios de ambos lados.

#Su utilidad tiene que ver con la posibilidad de limpiar el string para usar sus datos 
#en una BD

#Mandamos el mensaje a una variable para despues poder usar el metodo strip

nombre_usuario = "Administrador "

#Espacio en blanco hacia la derecha
print (nombre_usuario.rstrip())

nombre_empleado = " Juan Ocaso"

#Espacion en blanco hacia la izquierda

print (nombre_empleado.lstrip())

#strip sirve para borrar los espacios en blanco de ambos strings

nombre_alumno = " Ximena Vazquez "

print (nombre_alumno.strip())

varaible = ' Hola a todos mi nombre es Luis Alberto '

print (varaible.strip().upper().rstrip())

