#saber_el_numero_de_elementos_de_una_lista

lista_nombres_futbolistas = [] #Definimos una lista vacia

#Agregamos con append varios elementos a la lista previamente definida

lista_nombres_futbolistas.append('Toni Kross')
lista_nombres_futbolistas.append('Zinedine Zidane')
lista_nombres_futbolistas.append('CHicharito Hernandez')
lista_nombres_futbolistas.append('Lionel Messi')

#utilizamos el metodo len para saber que extension o cuantos elementos hay en la lista

#len va dentro o fuera del print, eso es irrelevante, lo importante es su parametro que es la lista

print (lista_nombres_futbolistas, len(lista_nombres_futbolistas)) #cuatro elementos en la lista

#Funciona len(nombrelista) incluso con elementos numericos de la lista

lista_deudas = [200.50, 570, 620.99]

print (len(lista_deudas)) #3 elementos en la lista

#len no es exlusivo de listas [] sino que tambien funciona con tuplas ()

tupla = (2,3,4,5)

print (len(tupla)) #Ahora sabemos la cantidad de elementos de una tupla

