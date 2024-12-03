#orden_listas_reversa

#para poder invertir el orden de una lista usamos el metodo reverse
#Reverse cambia el orden permanentemente, pero se puede regresar al original con otro reverse

#No confundir con sorted(reverse = True), pues ahí es el órden alfabetico al inverso.

lista = ['America', 'Pumas', 'Chivas']

print ('ORDEN ORIGINAL')

print (lista)

print ('ORDEN EN REVERSO')

lista.reverse() # Hacer en reversa el orden la de lista, por lo que ahora empieza por Chivas y termina en America

print (lista)

lista.reverse() #Para volver al orden original

print (lista)

#.reverse() lo que hace el cambiar el orden permanente, como lo hace sort()
