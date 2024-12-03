''''

usuarios = []

usuarios_registrados = len(usuarios)

print ('Numero de usuarios registrados en el sistema:', usuarios_registrados)

if usuarios_registrados == 0:
        print ('No hay usuarios registrados')

for usuario in usuarios:

    if usuario == 'admin':
        print ('Bienvenido, administrador, quiere imprimir un reporte detallado?')

    if usuario != 'admin':
        print('Bienvenido:, ', usuario.title())

'''

''''
usuarios_actuales = ['john', 'anselmi', 'julian', 'reynolds', 'hibrido', 'Reverendo']

usuarios_nuevos = ['ximena', 'ciego', 'victor', 'hibrido', 'Reverendo']

for nuevo in usuarios_nuevos:

    if nuevo in usuarios_actuales:
        print ('Nombre de usuario ya utilizado, seleccionar otro.')
    
    else:
        print ('Bienvenido.')

'''

numeros_ordinarios = [1,2,3,4,5,6,7,8,9]

for ordinal in numeros_ordinarios:

    if ordinal == 1:
        print ('1st')

    elif ordinal == 2:
        print ('2nd')

    elif ordinal == 3:
        print ('3rd')

    elif ordinal == 4:
        print ('4th')

    elif ordinal == 5:
        print ('5th')

    elif ordinal == 6:
        print ('6th')

    elif ordinal == 7:
        print ('7th')

    elif ordinal == 8:
        print ('8th')

    elif ordinal == 9:
        print ('9th')

    else:
        print ('Fin')


        
        

