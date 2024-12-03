#Otra parte de las condcionales if es el else, que nos permiten ejecutar codigo en caso de que lo 
#primero no suceda, haga otro bloque de código.

edad = 17

if edad == 18:
    print ('USTED ES MAYOR DE EDAD')
    print ('PUEDE EJERCER EL VOTO')

else: #En caso de que no se cumpla, enotnces haz esto, manda esta sentencia
    print ('USTED AUN NO PUEDE VOTAR, PUES ES MENOR DE EDAD')

#Las condicionales se pueden anidar, es decir colocar mas de una condicion dentro de diversas condiciones.

#Esto se hace mediante el comando elif

#PROGRAMA PARA ADMISION DE PERSONAS AL PARQUE DE DIVERSIONES. 

edad_visitante = 19

if edad_visitante <= 4:
    print ('Lamentablemente usted no puede ingresar al parque de diversiones.')

elif edad_visitante >5 and edad_visitante <=17: #Agregamos otra condicional, en la que aquel que tenga mas de 5 y menos de 17 pague 80 pesos
    print ('Bienvenido, su precio de boleto es de 80 pesos.')

elif edad_visitante >18:
    print ('Bienvenido, su precio del boleto es de 120 pesos') #Aquellos que tengan 18 o mas pagan boleto de 120 pesos

else:
    print ('Disfrute de su aventura.')
