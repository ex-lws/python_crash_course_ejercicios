#gente

gente = [] #Lista que almacernará diccionarios...

persona_1 = {'nombres' : 'angel',
             'apellido_paterno' : 'valiant',
             'apellido_materno' : 'raven',
             'edad' : 45
             }

persona_2 = {'nombres' : 'athur',
             'apellido_paterno' : 'godon',
             'apellido_materno' : 'pym',
             'edad' : 35
             }

persona_3 = {'nombres' : 'edgar',
             'apellido_paterno' : 'allan',
             'apellido_materno' : 'poe',
             'edad' : 21
             }

#Añado los diccionarios a la lista

gente.append(persona_1)
gente.append(persona_2)
gente.append(persona_3)

print (gente)

for persona in gente:
    print (persona)

#Mascotas
mascotas = []

mascota1 = {'nombre' : 'lucky',
            'tipo': 'perro',
            'raza': 'pug',
            'amo' : 'fererich starks'}

mascota2 = {'nombre' : 'dev',
            'tipo': 'gato',
            'raza': 'persa',
            'amo' : 'ronald spitelson'}

mascota3 = {'nombre' : 'daria',
            'tipo': 'perro',
            'raza': 'gran danes',
            'amo' : 'francheska dickens'}

mascotas.append(mascota1)
mascotas.append(mascota2)
mascotas.append(mascota3)

print (mascotas)

for mascota in mascotas:
    print ('\t' , mascota)

#Lugares favoritos

lugares_favoritos = {

    'angel' : {'california', 'mexico', 'new york'},
    'devon' : {'terracota', 'new jeresey', 'denver'},
    'killian' : {'francia', 'ciudad de mexico', 'freso'}
 }


for key, value in lugares_favoritos.items():
    print ('Los lugares favoritos de: ' + key.title() + ' son: ' + str(value))

#Numero favoritos.

numeros_favoritos = {

    'Charles' : {
        5, 4, 113
    },

    'randy': {

        200, 1, 77
    },

    'emerson' : {

        521, 0, 23

    }

}

print ('\n')

for key, value in numeros_favoritos.items():
    print ('Los numeros favoritos de: ' + key.upper() + ' son: ' + str(value))

#Ciudades

ciudades = {

    'ciudad de mexico' : {'pais': 'mexico', 'poblacion': 3000000},


    'nueva york' : {'pais' : 'usa', 'poblacion' : 10000000},

    'paris' : {'pais': 'francia', 'poblacion' : 1200000}

}

for key, value in ciudades.items():
    print ('Nombre de la ciudad: ' + key.upper() + ' y su informmacion es: ' + str(value))
