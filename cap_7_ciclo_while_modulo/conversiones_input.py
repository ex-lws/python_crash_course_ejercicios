#Como sabemos no es lo mismo string que int, ni int que float...

#Por lo tanto debemos tener claro que tipo de dato esperamos del usuario, 
#con el fin de manejar dicha informacion posterimente y evitar bugs o errores en el programa.

print ('Hola, bienvenido.')
print ('\nEste programa se encarga de convertid su edad humana a edad de perro.')
print ('\n')

edad = int(input ('Por favor escriba su edad:')) #Todo lo que el usuario escriba 
#se convierte a int, peus esperamos un número, la edad es un núemero entero

if edad <= 15:

    edad = str('6 meses')

    print ('Su edad de perro al tener 20 es de: ' + str(edad))

elif edad >= 20 and edad <27:

    edad = 1

    print ('Su edad de perro es: '+ str(edad) + ' año')

elif edad >= 28 and edad <=31:

    edad = 2

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 32 and edad <=35:

    edad = 3

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 36 and edad <=39:

    edad = 4

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 40 and edad <=43:

    edad = 5

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 44 and edad <=47:

    edad = 6

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 48 and edad <=51:

    edad = 7

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 52 and edad <=55:

    edad = 8

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 56 and edad <=59:

    edad = 9

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 60 and edad <=63:

    edad = 10

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 64 and edad <=67:

    edad = 11

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 68 and edad <=71:

    edad = 12

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 72 and edad <=75:

    edad = 13

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 76 and edad <=79:

    edad = 14

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 80 and edad <=83:

    edad = 15

    print ('Su edad de perro es: '+ str(edad) + ' años')

elif edad >= 84 and edad <=90:

    edad = 16

    print ('Su edad de perro es: '+ str(edad) + ' años')


else:
    print ('Su edad es de:' + str(edad))



