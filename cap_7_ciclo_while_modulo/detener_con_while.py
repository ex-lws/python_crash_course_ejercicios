print ('Bienvenido al servicio de almacenaje.')

print ('\nEscribe "enter" si quieres almacenar informacion.')
print ('\nEscribe "quit" si quieres cerrar el programa')

acceso = input()

if acceso == 'quit':
    print ('Fin del programa')

while acceso != 'quit':


    lista_valores = []

    mensaje_bienvenida = 'Hola, un gusto en verte.'

    print (mensaje_bienvenida)

    instrucciones = 'Escribe los valores a almacenar:'

    valores = int(input(instrucciones))

    lista_valores.append(valores)

    print ('Quieres seguir almacenando informacion: s/n')
    
    seguir = input()

    if seguir == 'n':

        print('Fin del programa')
        acceso = 'quit'

print ('Gracias')

print (lista_valores)


