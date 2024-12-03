#Podemos agregar diccionarios completos a una lista.

#Defino dos diccionarios con diversos elementos incluidos y que serán almacenados en una lista.

diccionario_teclados = {'marca': 'razer',
                        'escala': 'mini',
                        'color' : 'blanco'}

diccionario_pantallas = {'marca': 'hp',
                         'pugladas' : 32,
                         'panel': 'ips'}

#Ambos diccionarios los almaceno en una lista.

lista_diccionarios = []

#Los almaceno con append

lista_diccionarios.append(diccionario_teclados)
lista_diccionarios.append(diccionario_pantallas)

#Imprimo todos los valores almacenados con un for

for elemento in lista_diccionarios:
    print (elemento)

print (lista_diccionarios)

