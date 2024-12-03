#UN MODULO PUEDE TENER VARIOS MODULO QUE NOS INTERESEN...

#LA SINTAXIS PARA IMPORTAR UN MODULO ESPECIFICO ES: 
# from nombre_modulos import nombre_modulo_especifico

#EL AS ES PARA CAMBIARLE EL NOMBRE AL METODO ESPECIFICO EN LA CLASE ACTUAL UNICAMENTE, PERO NO ES NECESARIO 
#COLOCAR SIEMPRE EL ALIAS

#SI queremos importar todos los moodulos...
'''

from modulo_hacer_pizza import *

'''


from modulo_hacer_pizza import agregar_toppings_pizza as agregar_toppings

agregar_toppings('Peperoni', 'Salchicha', 'Masa delgada')


        