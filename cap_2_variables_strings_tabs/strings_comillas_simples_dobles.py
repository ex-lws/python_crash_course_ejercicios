#Podemos poner texto dentro de comillas o comillas simples
#Úitl para ser empleadas en cadenas de texto que las requieran.

alerta = "Por favor, cerrar el programa en caso de error" #Comillas dobles

alerta_3 = 'No me pidas que guarde mis pensamientos.' #Comillas simples

alerta_2 = 'Cerrar el programa si se presenta el error: "201"' #Comlillas simples y comillas dobles en un mismo string

print (alerta)

print (alerta_3)

print (alerta_2)

#Podemos usar metodos para poder cambiar la estructura gramatical de un string

titulo_libro = "el laberinto de la soledad"

#variableRTexto.title() es un metodo que lo que hace es convertir un strting a un texto 
#tipo titulo de obra

print (titulo_libro.title()) #el metodo .tittle() lo que hace es convertir a titulo

#varaibleTexto.lower() permite cambair todo a minusculas

apellido = "REYES"

print (apellido.lower()) #el metodo .lower() lo que hace es convertir a minusculas

#variableTexto.upper() lo que hace es cambiar todo a mayusculas

nombre = "luis alberto"

print (nombre.upper()) #el metodo .upper() lo que hace es convertir a mayusculas
