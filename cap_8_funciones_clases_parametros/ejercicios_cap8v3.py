#MAGOS.

def imprimir_mago(magos): #IMPRIMO CADA UNO DE LOS ELEMENTOS DE LA LISTA COMO PARAMETRO

    for mago in magos:

        print (mago)

#USO COMO PARAMETRO UNA LISTA DE 3 MAGOS.

magos_historicos = ['oz', 'dojini', 'peanwy']

imprimir_mago(magos_historicos[:]) #HACER UNA COPIA DE LA LISTA ORIGINAL O O NO AFECTARLA.

def hacer_grande(magos, amgos_grandes): #ARGEGO UNA NUEVA LISTA QUE PARTE DE LA PRIMERA Y AGREGA UN TEXTO A LOS ELEMENTOS.

    for mago in magos:

        magos_grandes =  ['El gran: ' + mago]
        print (magos_grandes)

hacer_grande(magos_historicos, []) #IMPRIMO LA NUEVA LISTA CON LOS TEXTOS NUEVOS.

print (magos_historicos) #IMPRIMO UNA COPIA DE LA ORIGNAL, QUE AUN TIENE SUS ELEMENTOS OIRGINALES GRACIAS A [:]