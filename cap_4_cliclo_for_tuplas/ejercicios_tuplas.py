buffet = ('romeritos', 'arroz', 'chicharron', 'carnitas', 'atun')

for elemento_bufet in buffet:
    print (elemento_bufet)

print (buffet[0:2])

print (buffet)

buffet_neuvo = ('ensalda rusa', 'arroz', 'chicharron', 'filete de pescado', 'atun') 

#renombro la tupla.

buffet = buffet_neuvo

#Sólo podemos cambiar el nombre de la tupla, agregar y quitar elementos es imposible.

print ('Nuevo buffet con reemmplazos:', buffet_neuvo)
