#listas

#Una lista es una coleccion de elementos, pueden ser strings o numeros. 
#Los elementos se separan por comas y van dentro de corchetes []

#Una de las caracterisiticas de las listas, es que estas se pueden alterar, 
#es decir, se pueden borrar, agregar elementos.
#Incluso cambiar su orden permanentemente, al contrario que con las tuplas que son inmutables.

marcas_pc = ["HP", "Dell", "Apple", "Lenovo"] #Lista de strings

print (marcas_pc) #Imprimimos la lista

precios_laptop = [2500, 2800, 3200] #Lista de numeros enteros

print (precios_laptop) #Imprimimos la lista


precios_boletos = [755.25, 820.75, 999.99] #Lista con numeros flotantes

print (precios_boletos) #Imprimimos la lista


#Podemos acceder a los elementos de la lista, invidivualmente con el uso del index y 
#el numero del elemento, que comienza en 0
#O bien podemos usar numeros negativos para empezar a contar de derecha a izquierda 
#el numero de elementos en la lista 

#Sintaxis = nombreLista[indice]

alumnos = ["luis alberto", "juan carlos", "ximena", "lizeth artziri"]

#Imprimir unicamente el tercer elemento de la lista

print ("El alumno@: " + alumnos[-2].title() + ", ha reprobado el curso.") #Podemos usar numeros negativos para poder imprimir algun elemento, contando de derecha a izquierda

#Imprimir el primer elemento de la lista

print ("El alumn@: " + alumnos[0].title() + " ha aprobado el curso.")

#A los elelemtnos de la lista podemos concatenarlos y ponerles metodos para hacerlos en mayusculas, minusculas, etc

marcas_jabones = ["Terso", "grisi", "escudo", "cetaphil", "aquasoap"]

ganador = "\n\tEl mejor jabon de este año 2024 es..." + " " + marcas_jabones[0].upper() + ", felicidades."

print (marcas_jabones, ganador)


