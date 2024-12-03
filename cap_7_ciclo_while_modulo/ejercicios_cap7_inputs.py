#Renta de autos

print ('Bienvenido al programa de seleccion de renta de autos.')

instrucciones = '\nPor favor escriba el auto que quiere rentar.'

auto_seleccionado = input (instrucciones)

print ('\nBuscado si esta disponible el auto: ' + str (auto_seleccionado))

#Reservacion dependiendo el numero de personas para la mesa

print ('Bienvenido al Great Palace.' + '\nEn un momento le asignamos su mesa...')

pasos = '\n\tPor favor, escriba la cantidad de invitados que acudiran al restaurante.'

cant_invitados = int (input(pasos))

if cant_invitados >= 8:

    print ('Al ser 8 o mas invitados, ustedes tendran que reservar fisicamente.')

else:
    print ('\nMesa asignada correctamente, consulte su correo electronico.')

#multiplos de 10

lista_resultados = []


for resultado in range (0, 11):
    resultado_tabla = 10 * resultado
    lista_resultados.append(resultado_tabla)


mensaje_vbienvenida = 'Hola, te dire si el numero que estas escribiendo es multiplo de 100...'
indicacion = 'Por favor escribe el numero:'

print (mensaje_vbienvenida)
print ('\n')

numero_usuario = int(input(indicacion))

if numero_usuario in lista_resultados:
    print ('Su numero es un multiplo de 10')

else:
    print ('Su numero no es multiplo de 10')

