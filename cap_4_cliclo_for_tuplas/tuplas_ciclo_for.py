#Las tuplas son basicamente listas, pero que su contenido una vez definido no se puede modificar despues 

#Las tuplas se caracterizan por usar parentesis en lugar de corchetes, a sus elementos se les llama inmutables
#No se pueden modificar,pero si realziar operacones estadisiticas sobre ellos.

#La unica manera de alterarlas es mediatne su renombración.

medidas_rectangulo = (25, 75)


#Podemos imprimir los elementos de la tupla mediante su indice al igual que se hacía con las listas.

print (medidas_rectangulo)
print (medidas_rectangulo[0])
print (medidas_rectangulo[1])

#Comrpobamos que no podemos agregar como si se puede con las listas

# medidas_rectangulo.append (2)
# medidas_rectangulo.insert(0, 6)
# medidas_rectangulo(0) = 7

#Podemos usar una tupla como rango para un ciclo for

for medida in medidas_rectangulo:
    print (medida)

#La unica manera de alterar una tupla es renombrarla y agregar o cambiar los valores

print ('tupla original', medidas_rectangulo)

nuevas_medidas_rectangulo = [10, 25]

medidas_rectangulo = nuevas_medidas_rectangulo

print ('Nueva tupla', medidas_rectangulo)

#En conclusions las tuplas, son basicamente un conjunto de elementos que van encerrados entre parentesis y son inmutables.
#Una vez definida la tupla, no se puede modificar mediante otros comandos posteriores en el flujo del programa.
