#Veamos otro ejemplo de diccionarios que almacenan diccionarios

#Definimos un diccionario de autos y agregamos dos autos con sus respectivas 
#caracteristicas.

autos = { #diccionario de autos, con dos diccionarios de auto independiente.

    'Ferrari F40' : {
        'color': 'rojo',
        'motor' : 'traccion trasera',
        'precio' : 50000000
    },

    'Toyota Yaris GR' : {

        'color': 'negro',
        'motor' : 'traccion total',
        'precio' : 10000000
    }
}

'''

De esta manera imprimimos mediante un for los valores de las key y los values de ambos diccionarios...

for key, value in diccionario.items() = Recorreá tanto keys y values de ambos diccionarios.

'''

for key, value in autos.items(): #Mandamos a imprimir el nombre de los autos y 
    #ademas una carcacteristica especifica.

    print ('Auto almacenado: ' + key)
    print ('Color disponible: ' + str(value['color']))
    print ('precio: ' + str(value['precio']))
    print ('\n')