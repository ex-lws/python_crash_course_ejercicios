'''

try except es una instruccion para Python que nos permite poder intentar hacer algo en el programa
y si en dado caso hay un error esperado, hacer uso de un try y contiunar con el flujo del programa...


Es beneficioso pues permte que el usiario vea errores amigables y el programa no truene, coloquialmente hablando.

'''


#DIVISION POR CERO = ES IMPOSIBLE 

#print (5 / 0) #MANDA ERROR, TRACEBACK, NO SE PUEDE DIVIDIR POR CERO

try: 
     print (5/0)

except ZeroDivisionError:

     print ("Usted no puede dividir por cero...") #NO MUESTRA ZERODIVISIONERROR...
     #MUESTRA ESTE MENSAJE AL USUARIO.


'''

TODO EL CODIGO A PARTIR DE AQUI SE EJECUTARA DESPUES DEL TRY EXCEPT

'''