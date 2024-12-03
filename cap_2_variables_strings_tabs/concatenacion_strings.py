#Podemos concatenar diversos mensajes con el signo + 
#La concatenacion es util para solo juntar strings y crear un mensaje más completo.

#Todo lo que va dentro de comillas dobles o simples es un string.

#NO SE PUEDE CONCATENAR TEXTO O STRINGS CON INT O FLOATS, ES DECIR NUMEROS.
#PARA ELLO REQUIERE CONVERSION = str(valorNumerico)

nombre = "luis alberto"
edad = 19 #Podemos en lugar de usar el int, usar un string "19" y no habría problema.
ciudad = "ixtapaluca"

print ("Bienvenido:" + " " + nombre.title() + ", usted tiene:" + str(edad) + " años" + "" + " y vive en: " + ciudad.title())
print (nombre + str(edad) + ciudad)
