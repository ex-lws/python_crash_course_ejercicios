#Podemos usar otra union de condiciones, la cual se llama or

#esta funciona para comparar dos posibles condiciones y si tan solo una se cumple, 
#entoces realiza el codigo del if

#Definimos nuestras variables

licencia_conducir = True

edad = 16

print ('Su edad es de: ' + str(edad))

if licencia_conducir == True or edad >= 18: #or va en medio de las dos condiciones, por lo que, 
    #si tan solo una se cumple, se imprime la sentencia dentro del if

    print ('Bienvenido a nuestro clandestino casino.' + 
           '\t\nUn lugar verdaramente lleno de adictos.')
    
if licencia_conducir == False or edad <18:

    print ('Lo lamento, usted aun no puede ser un ludopata que valga la pena.')
    
print ('Fin del if')

