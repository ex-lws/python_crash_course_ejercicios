##ejercicio_listas_capitulo_3

lugares_anhelados = ['Berlin', 'Napoles', 'Milan', 'Roma', 'Escocia']

print (lugares_anhelados)

print (sorted(lugares_anhelados)) #Orden alfabetico, pero sin modifcar

print (lugares_anhelados) #Orden original

print (sorted(lugares_anhelados, reverse= True))#Orden alfabetico inverso, pero sin modificar

print (lugares_anhelados) #Orden original

lugares_anhelados.reverse() #Orden cambiando a reversa permanentemente

print (lugares_anhelados)

lugares_anhelados.sort() #Orden alfbaetico permamente


print (lugares_anhelados) 

lugares_anhelados.sort(reverse=True) #Orden alfabetico al reves permanente

print (lugares_anhelados) #Orden alfabetico al reves permanente

#Lista de invitados

lista_invitados = ['Juana', 'Carmen', 'Harumni', 'Luis']

print (len(lista_invitados)) #Cantidad de elementos de la lista

#Ejercicio final

lista_paies = ['Mexico', 'Alemania']

print (lista_paies)

lista_paies.append('Holanda')

lista_paies.insert (0, 'Inglaterra')

print (lista_paies)

pais_no_europero = 'Mexico'

lista_paies.remove(pais_no_europero)

print (lista_paies)

lista_paies.append ('Rusia')

lista_paies.append ('Belgica')

print (sorted (lista_paies))

print (lista_paies)

print (len(lista_paies))

del lista_paies [0]

print (lista_paies)

lista_paies.sort()

print (lista_paies)
