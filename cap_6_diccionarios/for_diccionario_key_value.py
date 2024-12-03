#Podemos usar ciclos for para poder iterar en los elementos de un diccionario.

#Definimos un diccionario...

usuario = {'nombre': 'leviatan777',
           'edad': 27,
           'ubicacion': 'amsterdam'
           }

#la llave es el titulo del atributo y el valor es aquello que almacena el atributo.

#key y value son variables temporales que recorreran las mismas key y value del diccionario.

#se separan por comas

#.items() indica que recorrerá key y value

for key, value in usuario.items():

    #print (key.upper() + ': ' + str(value))

    print ('LLAVE: ' + key)
    print ('\n')
    print ('VALOR DENTRO DE LA LLAVE: ' + '\t' + str(value))
    print ('\n')

#Replicar el ejemplo, colocando nomrbes de personas y su predileccion por algun lenguaje de programacion.

lenguajes_personas = {}

lenguajes_personas['maria'] = 'c#'
lenguajes_personas['luis'] = 'python'
lenguajes_personas['joel'] = 'javascript'
lenguajes_personas['randal'] = 'java'

print ('Diccionario completo: ', lenguajes_personas)

print ('Imprimiendo mensaje personalizado...' + '\n')

for key, value in lenguajes_personas.items():
    print ('El lenguaje favorito de: ' + key.title() + ' es: ' + str(value.upper()))

#Podemos loopear únicamente las llaves...

print ("***NOMBRES DE LAS PERSONAS EN EL DICCIONARIO***")

for nombre in lenguajes_personas.keys():
    print (nombre.title())

#Ahora podemos loopear unicamente los values del diccionario

print ("***IMPRIMIENDO LOS LENGUAJES DE PROGRAMACION EN EL DICCIONARIO")

for lenguaje in lenguajes_personas.values():

    print (lenguaje.title())
