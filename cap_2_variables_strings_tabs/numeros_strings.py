#numeros en strings
#Conversiones al concatenar

edad = 23 #Entero

edad_string = "23" #String o texto, no requiere de conversión para concatenar.

#print ("Tu edad es de: " + edad " años") MANDA ERROR, PORQUE EDAD CONTIENE UN ENTERO

#No podemos concatenar strings con numeros ni nummeros con strings para hacerlo 
#debemos de realziar una conversion con la funcion str(variable entera), de esta manera el int se muestra como string.

print ("Tu edad es de: " + edad_string + " años.") #Funciona correctamente, 
#pues 23 es un string y por lo tanto lo podemos concatenar

#Podemos solucionar este error, trabajando con una funcion str, que convierte un int 
#o float a string

print ("Tu edad es de: " + str(edad) + " años.")

salario = 17500 

print ("Su salario actual es de: " + str(salario) + " pesos.")

bono_horas_extra = 500.50

salario_total = salario + bono_horas_extra

print ("Su bono es de: " + str(bono_horas_extra) + "y su salario total es de: " + str(salario_total))

#Otra forma de concatenar sin acudir al str() es...
#Mediante el uso de la coma, que separa una variable con su string de la entera

#Esto es recomendable para resultado rápidos

mensaje_error = 'El programa se cerro inesperadamente. Error: '

error = 607

print (mensaje_error, error)

