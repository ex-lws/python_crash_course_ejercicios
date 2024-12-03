#Podemos unicamente iterar los valores de las llaves, no con .items() sino con .keys()

diccionario_pc = {'hp': 'mala',
                  'dell': 'buena',
                  'asus': 'muy buena'}

#quiero iterar solo las keys, por eso el .key()

for pc in diccionario_pc.keys():
    print ('Las marcas de PC almacenadas en el diccionario son: ' + pc.upper())