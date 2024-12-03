import unittest
from ciudad_pais import formatear_ciudad

class PruebaFormatearCiudad(unittest.TestCase):

     def probarMetodo(self):

          ciudad_formateada = formatear_ciudad('ciudad de mexico', 'mexico')

          self.assertEqual (ciudad_formateada, 'Santiago, Chile')

unittest.main()