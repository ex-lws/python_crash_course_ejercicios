'''

Puede que al momento de pedirle un dato al usuario, tengamos a posibilidad de esperar algún tipo de dato...
Sin embargo sucede que el usario coloca otro tipo, por lo que el programa no funciona.
Cachar ese error es vital para que el programa funcione

'''

instrucciones_valor_1 = "Por favor, escriba el primer valor"
instrucciones_valor_2 = "Por favor, escriba el segundo valor"

#MEDIANTE INT(INPUT()) = CONVERTIMOS TODO TIPO DE TEXTO A INT

try:

     valor1 = float(input (instrucciones_valor_1))

     valor2 = float(input(instrucciones_valor_2))

     resultado_suma = (valor1 + valor2)

     print ("El resultado obtenido ese de: " + str(resultado_suma))
     

except ValueError:

     print ("Por favor, sólo escriba números en los campos de entrada.")