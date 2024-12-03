#diccionario de una persona

hermana = {'nombres' : 'ximena devone', 'apellido materno' : 'shortcut', 'apellido paterno' : 'levys', 'edad' : 23, 'ciudad': 'new york' }

print ('ATRIBUTOS GUARDADOS EN EL DICCIONARIO:')

#Imprimo las keys que me interesan.

print (hermana['nombres'])
print (hermana['apellido materno'])
print (hermana['apellido paterno'])
print (hermana ['edad'])
print (hermana['ciudad'])

print ('diccionario integro: ' + str(hermana))

#numeros favoritos

numeros_favoritos = {'angel': 5, 'luis' : 13, 'maura' : 10, 'maria' : 2}

print (numeros_favoritos)

#Agregar numeros de mas amigos a fin de agregar mas datos.

numeros_favoritos['Devon'] = 77
numeros_favoritos['randal'] = 66

print (numeros_favoritos)
print ('\n')

#glosario

glosario = {'lista' : 'conjunto de elementos que se pueden eliminar, reemplazar y hacer crecer',
            'tuplas' : 'serie de elementos inmutables',
            'ciclo for' : 'loop o bucle que permite iterar por medio de un rango o una lista',
            'condicional if': 'permite ejecutar codigo si se cumple o no una serie de condiciones',
            'diccionarios': 'permiten guardar informacion y asignarla a una llave pre-nombrada al estilo de na base de datos',
            }

for elemento in glosario:

    print (elemento.upper() + ': ' + '\n' + '\t' + glosario[elemento].lower())

#Lenguajes

lenguajes_personas = {}

lenguajes_personas['maria'] = 'c#'
lenguajes_personas['luis'] = 'python'
lenguajes_personas['joel'] = 'javascript'
lenguajes_personas['randal'] = 'java'

lista_nuevos = ['john', 'raven', 'joel', 'killian']

for nombre in lista_nuevos:

    if nombre in lenguajes_personas:
        print ('Nombre ya en el diccionario...')

    else:
        print ('Agregando usuario...')
