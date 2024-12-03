#Ahora veremos como poder saltar linea en python

#Podemos saltar linea utilizando '\nMENSAJE' 
#El \n que salta la linea va justo 
#despues de la apertura de las comillas del string

#Saltar la linea quiere decir bajar un renglon coloquialmente hablando.

print ("Las cosas que menos me gusta comer: " + "\n\tPollo\n\tChiles rellenos\n\tChayote")

#Para poder escribir en una nueva linea utilizamos el siguiente simbolo que es \n

print ("Hola queridos alumnos, esta es mi lista de aprobados:" + "" + "\nLuis Alberto Reyes Cruz \nMariana Itzel Reyes Cruz" + "\nSaludos.")

#Podemos saltar la linea con \n y despues tabular con \t, es decir combinar tanto \n y \t en un mismo string.

print ('\n\tEsto es Mexico, cabrones...')

'''
Podemos realizar una concatenación de varios \t y \n

'''

mensaje_personalizado = "Hoy parece ser un buen día" + "\nHace un buen clima, lindo cielo..." + "\n\tTal vez ser buena idea hacer ejercicio."

print (mensaje_personalizado)
