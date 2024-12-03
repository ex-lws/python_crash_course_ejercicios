lista_numeros = []

for valor in range (0, 11, 2):
    lista_numeros.append(valor)

print (lista_numeros)
print (max(lista_numeros)) #Imprime el valor máximo en la lista, el más grande
print (min (lista_numeros)) #Imprime el valor más pequeñ de la lista.
print (sum(lista_numeros)) #Suma todos los elementos de la lista y obtiene un resultado

#Creo una lista que es vacia en principio, despues agrego un ciclo for para iterar 10 veces del 
#0 al 10
#Dichos valores de conteo se agregaran a la lista

#Imprimo en consola el contenido de la lista, el valor maximo, minimo y la suma de todos los 
#valores juntos

#Estas opciones igual funcionan en tuplas...

tupla_salarios_ultimo_año = (2500, 7200, 500, 600, 12900)

print (tupla_salarios_ultimo_año)

print (max(tupla_salarios_ultimo_año))

print (min(tupla_salarios_ultimo_año))

print (sum(tupla_salarios_ultimo_año))

