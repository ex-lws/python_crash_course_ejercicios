#RIOS

rios_grandes = {}

rios_grandes['rio sena'] = 'francia'
rios_grandes['rio volga'] = 'rusia'
rios_grandes['rio tamesis'] = 'inglaterra'
rios_grandes['rio garona'] = 'francia', 'espana'

for key, value in rios_grandes.items():
    print ('El '  + key.title() + ' corre en '+ str(value))

#rios en el diccionario, uicamente las llaves.

for rio in rios_grandes.keys():
    print (rio)

#paises donde corren los rios, unicamente los values.

for pais in rios_grandes.values():
    print (pais)
    
    
ciudades_mexico = {"Iztacalco" : "Oriente", "Iztapalapa" : "oriente"}

for key, value in ciudades_mexico.items():
	
	print (key, value)
