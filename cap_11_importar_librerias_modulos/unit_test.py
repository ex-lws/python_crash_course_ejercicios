'''

UNIT TESTS es colocar la salida que esperamos de un metodo, puede haber muchos casos por lo que es importante hacer muchas pruebas o test de unit

'''

import unittest #IMPORT LA CLASE UNIT TEST PARA LAS PRUEBAS DE UNIDAD

from formatear_nombre import formatearNombre #IMPORTO EL MODULO QUE QUIERO TESTEAR

#CREAMOS UNA CLASE QUE PORBARA EL METODO O FUNCION COMO PARAMETRO: UNITTEST.TESTCASE

class PruebaFormatearNombre (unittest.TestCase):

     '''REALIZA UNA PRUBEA DE LA FUNCION FORMATEAR NOMBRE'''

     #METODO QUE PRUEBA UN ASPECTO DE LA FUNCION A PROBAR

     def prueba_nombre_formato(self):
        
        #BUSCAMOS QUE EL METODO ORIGINAL PRODUZCA UNA SALIDA
        
        nombre_formateado = formatearNombre('luis alberto', 'reyes', 'cruz')

        #USAMOS EL METODO ASSERT PARA QUE LA SALIDA SEA DEL METODO ANTERIOR SEA
        #IGUAL O PARECIDA AL ASSERT, QUE LA COMPARARA CON LA DEL METODO

        self.assertEqual(nombre_formateado, 'Luis Alberto Reyes Cruz')

#unittest.main () LE INDICA A PYTHON QUE CORRA O EJECUTE LA PRUBA DE UNIDAD

unittest.main()

'''

Las pruebas y en especial las pruebas de unidad son para poder comparar la salida esperada
con la salida que un metodo o funcion puede producir.

Si no sucede, se debe modificar el metodo...

'''