#PARA PODER AGREGAR UN MODULO O FUNCION INDEPENDIENTE, HACEMOS USO DE LA SINTAXIS: import nombreModulo

#POR LO REGULAR LAS IMPORTACIONES SIEMPRE VAN ARRIBA DE LA CLASE O DEL PRGRAMA.

import modulo_hacer_pizza #IMPORTANCION DEL MODULO

#PODEMOS PONERLE UN ALIAS AL MODULO CON AS SEGUIDO DEL NUEVO NOMBRE

'''
import modulo_hacer_pizza as crear_pizza 

'''


#PARA PODER HACER USO DEL MODULO, LO QUE HACEMOS ES LLAMARLO Y COLOCAR. PARA DESPUES COLOCAR SUS ARGUMENTOS 
#NECESARIOS PARA INSTANCIARLO

#SINTAXIS = nombreModulo.nombreFuncion (parametros)

modulo_hacer_pizza.agregar_toppings_pizza('Peperoni', 'Champinones', 'Masa rellena de queso')