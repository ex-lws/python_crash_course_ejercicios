#Herencia es basicamente heredar todas caracteristicas de una clase juntos con sus metodos en otra clase
#El objetivo es poder usar sus caracterisicticas y sumarle más cosas nuevas a fin de crear una clase nueva

#Clase padre y clase hijo, el hijo hereda de la clase padre...

'''

La herencia permite la reutilización de código a fin de utilizar las fucionalidade de una clase en otra sin escribir todo de nuevo.

'''

class Auto ():

     def __init__(self, marca, modelo, año):

          """Inicizalizamos los atributos"""

          self.marca = marca
          self.modelo = modelo
          self.año = año
          #parametro por default

          self.kilometraje = 0
          self.litros_gasolina = 20
     
     def desplegar_info_auto (self):

          """Mostrar información formateada del auto"""

          info_auto = self.marca + " " + self.modelo + " " + str(self.año)

          print (info_auto.title())

     def mostrar_kilometros (self):

          print ("El kilometraje del auto es de: " + str(self.kilometraje) + " kilometros")

     def mostrar_litros_gas(self):

          print ("La cantidad de litros de gasolina del auto es de: " + str(self.litros_gasolina))

     #PODEMOS MODIFICAR UN PARAMETRO MEDIANTE OTROS METODOS 

     def actualizar_kilometraje(self, kilometraje):

          self.kilometraje = kilometraje

#La herencia hace referencia a la capacidad de una subclase de poder heredar atributos y metodos de la clase super.
#La herencia permite trabajar y crear metodos nuevos tomando en cuenta los anteriores de la clase super.

'''
LA CLASE HIJA HEREDA A CLASE PADRE...

'''


class Auto_electrico (Auto): #Dentro colocamos la clase padre

     def __init__(self, marca, modelo, año): #Atributos de la clase padre

     #Heredamos los atriburos de la clase padre a la clase hija con super; constructor

          super().__init__(marca, modelo, año)
          
          #Agregamos un nuevo parametro, pero úncio de la clase hija o subclase.

          self.tamaño_bateria = 70


     def mostrarBateria(self):

          #Podemos crear metodos para trabajar con atributos unicos de la subclase

          print ("La cantidad de batería del auto eléctrico es: " + str(self.tamaño_bateria) + " kilo whats.")

          #Podemos incluso trabajar con los metodos originales y cambiar su comportamiento

     def mostrar_litros_gas(self):
          
          print ("Los autos electricos no tienen tanques de gas")

     

#Basicamente lo que hacemos es herededar atributos, metodos y datos de la clase padre...
#Los parametros, atributos y metodos de la subclase son unicas de la subclase, no son parte de la clase padre.
#El objetivo es evitar que se usen metodos que van deacuerdo a los estandares de la clase hija.

tesla = Auto_electrico("tesla", "model - s", 2018)
tesla.desplegar_info_auto()
tesla.mostrar_kilometros()
tesla.mostrarBateria()
tesla.mostrar_litros_gas()

'''

CLASE PADRE = AUTO, CLASE HIJA = UN AUTO, QUE TIENE IGUALES CARACTERISTICAS, PERO ES ELECTRICO.


'''