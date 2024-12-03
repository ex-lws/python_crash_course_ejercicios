#Podemos iterar solo los values de las keys mediante el uso del metodo .values()

diccionario_autos = {'ferrari' : 5,
                     'renault' : 15,
                     'merdeces': 10}
                    
#.values() iterará sólo values del diccionario.

for auto in diccionario_autos.values():
    print ('La cantidad de autos de cada marca es: ' + str(auto))
