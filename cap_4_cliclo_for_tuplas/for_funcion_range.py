#Podemos usar la funcion range para poder iniciar un conteo de numeros
#El primer valor es el inicial, el segundo el final, el tercero es el incremento

#Igual el range es indicar la cantidad de veces que queremos iterar algo dentro del for.

#Sintaxis = for variableTemporal in range (inicio, final, incremento):

for valor in range (0, 11): #Para cada valor en el rango de 0 a 11 imprime su contenido #10 VECES
    #print (valor)
    print (valor * 5) #A cada valor, desde el 0 al 10 para obtener la tabla completa del 5.

lista_numeros = list(range (0, 50, 2)) #Crea una lista del 0 al 50, que contenga valores de 2 en 

#El tercer valor es el incremento del rango.

print (len(lista_numeros))
print (max(lista_numeros))
print (lista_numeros)

lista_ejemplo = [] #Defino una lista vacia, en la que se agregaran mas tarde algunos elementos

for valor in range (0, 21): #defino un for que iterara 20 veces

    lista_ejemplo.append (valor) #Podemos meter los valores del for a una lista, aquello que recorrá...

print (lista_ejemplo)

