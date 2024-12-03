#aliens

#Version que te da 5 puntos

aliens = ['verde', 'amarillo', 'rojo']

aliens = 'amarillo' #Elegir el elemento.

if 'verde' in aliens:
    print ('Ganaste 5 puntos')

elif 'amarillo' in aliens:
    print ('Ganaste 10 puntos')

elif 'rojo' in aliens:
    print ('Ganaste 15 puntos')

#edades

edad = 178

if edad <2:
    print ('eres un bebe.')

elif edad >2 and edad <=4:
    print ('Usted es un nino pequeno')

elif edad >4 and edad <= 13:
    print ('Usted es un nino')

elif edad >13 and edad <= 20:
    print ('Usted es una adolescente.')

elif edad >20 and edad <= 65:
    print ('Usted es un adulto.')

elif edad > 65 and edad <= 130 : 
    print ('Usted es un anciano.')

else:
    print ('Usted ha vivido demasiado...')

#Frutas

frutas_fav = ['fresa', 'banana', 'coco', 'kiwi', 'lichies']

if 'fresa' in frutas_fav:
    print ('Base de mermeladas y postres.')

if 'banana' in frutas_fav:
    print ('Clave para evitar calambres.')

if 'coco' in frutas_fav:
    print ('Maginifa para realizar bebidas refrescantes.')

if 'kiwi' in frutas_fav:
    print ('Acido, pero dulce por igual.')

if 'lichies' in frutas_fav:
    print ('Alimento de los dioses.')

else:
    print ('fin del programa.')