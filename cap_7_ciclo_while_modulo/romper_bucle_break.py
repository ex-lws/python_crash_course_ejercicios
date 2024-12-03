#Podemos romper un bucle utilizando break

#break significa que se detiene el while si algo pasa

print ('Bienvenido.')
print ('Escriba "quit" si quiere salir del programa.')

activador = True

ciudades_almacenadas = []

while activador:

    
    ciudad_usuario = input('Escriba su ciudad: ')

    print (ciudad_usuario + ' Esa es una ciuadad muy hermosa')

    ciudades_almacenadas.append(ciudad_usuario)

    if ciudad_usuario == 'quit':
        break #DETENER EL BUCLE

print ('fin del programa')
print ('Datos almacenados:', ciudades_almacenadas)