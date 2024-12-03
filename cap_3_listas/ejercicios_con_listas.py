#ejercicios_con_listas 
#ejercicios de libro

lista_invitados = ["Mariana Itzel", 'Maria Lobato', 'Octavio Guerra', 'Rufus']

print ('Hola querida, ' + lista_invitados[0] + ' te envio este mensaje para invitarte a cenar')
print ('Hola querida, ' + lista_invitados[1] + ' te envio este mensaje para invitarte a cenar')
print ('Hola querido, ' + lista_invitados[2] + ' te envio este mensaje para invitarte a cenar')
print ('Hola querido, ' + lista_invitados[3] + ' te envio este mensaje para invitarte a cenar')

print ('Lamentablemente nuestro invitado, ' + lista_invitados[2] + ', no podra asistir a la cena')

lista_invitados[2] = 'Ermelinda Linda' #Renombrar elemento

print (lista_invitados)

print ('Mediante esta nueva invitacion, espero que asistas a la cena del miercoles, querida ' + lista_invitados[0] + '.')
print ('Mediante esta nueva invitacion, espero que asistas a la cena del miercoles, querida ' + lista_invitados[1] + '.')
print ('Mediante esta nueva invitacion, espero que asistas a la cena del miercoles, querida ' + lista_invitados[2] + '.')
print ('Mediante esta nueva invitacion, espero que asistas a la cena del miercoles, querido ' + lista_invitados[3] + '.')

print ('Mediante este mensaje les informo que he encontrado una mesa mucho mas grande, por lo que habra nuevos invitados')

lista_invitados.insert(0, 'Angelica Mercado alias "La Maligna"')
lista_invitados.insert(2, 'Reinaldo Lara de Azteca Noticias')
lista_invitados.append('Charles Leclerc')

print (lista_invitados)

print ('Tu mesa esta colocada justo en el centro, es la mas grande, querido: ' + lista_invitados[0])
print ('Tu mesa esta colocada justo en el centro, es la mas grande, querido: ' + lista_invitados[1])
print ('Tu mesa esta colocada justo en el centro, es la mas grande, querido: ' + lista_invitados[2])
print ('Tu mesa esta colocada justo en el centro, es la mas grande, querido: ' + lista_invitados[3])
print ('Tu mesa esta colocada justo en el centro, es la mas grande, querido: ' + lista_invitados[4])
print ('Tu mesa esta colocada justo en el centro, es la mas grande, querido: ' + lista_invitados[5])
print ('Tu mesa esta colocada justo en el centro, es la mas grande, querido: ' + lista_invitados[6])

print ('Desafortunadamente solo podre invitar a dos personas a la cena')

primer_eliminado = lista_invitados.pop() #Borra el ultimo...
print ('Lo siento, ya no estas invitado, ' + primer_eliminado)

segundo_eliminado = lista_invitados.pop()
print ('Tambien estas desinvitado de la cena, ' + segundo_eliminado)

tercer_eliminado = lista_invitados.pop()
print ('Lo siento, tu tampoco sigues invitado ' + tercer_eliminado)

cuarto_eliminado = lista_invitados.pop()
print ('Lo siento, tu tampoco sigues invitado ' + cuarto_eliminado)

quinto_eliminado = lista_invitados.pop()
print ('Lo siento, tu tampoco sigues invitado ' + quinto_eliminado)

print (lista_invitados)

lista_invitados.remove('Angelica Mercado alias "La Maligna"') #Rquiere de value exacto.
lista_invitados.remove('Mariana Itzel')

print (lista_invitados)