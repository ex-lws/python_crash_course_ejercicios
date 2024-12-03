#Usar un for para imprimir los valores del 1 al 20

for valor in range (0, 21):

    print (valor)

#Lista del 1 al millon

lista_grande = []

for valor in range (1, 1000001):
    print (valor)
    lista_grande.append(valor)

print (lista_grande)

#Encuentra los valores maximos, minimos y sumalos todos de la lista de 1000000

print (max(lista_grande))
print (min(lista_grande))
print (sum(lista_grande))

#numeros primos

for primo in range (3, 21, 2): #El incremento es de 2 en 2 hasta el 20

    print (primo)

#Tabla del 3

lista_tabla_3 = [valor * 3 for valor in range (0, 11)]

print (lista_tabla_3)

#Imprimir los primeros 10 cubos

for cubo in range (0, 11):
    cubo = cubo ** 3
    print (cubo)

#Los 10 primeros cubos en una list comprehension

lista_cubos_10 = [valor ** 3 for valor in range (0, 11)]

print (lista_cubos_10)