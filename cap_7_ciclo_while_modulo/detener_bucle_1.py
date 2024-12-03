#Podemos detener el bucle si en algun momento lo que lo inició lo cambia.

activador = True #ACTIVADOR

valor = 1 #DEFINO UNA VARIABLE DE PRUEBA

while activador:

    print ('Entrando el bucle')

    valor += 1 #Sumará infinitamente 1 a valor

    print (valor)

    seguir = input ('s/n para seguir sumando') #Condición para romper el bluce.

    if seguir == 'n':
        
        activador = False #Rompo el bucle al cambiar el activador a false.
    
