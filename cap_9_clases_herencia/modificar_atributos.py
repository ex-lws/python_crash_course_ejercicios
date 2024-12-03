#Podemos modificar los atributos de las clases directamente o bien mediante metodos

class Auto ():

     def __init__(self, marca, modelo, año):

          """Inicizalizamos los atributos"""

          self.marca = marca
          self.modelo = modelo
          self.año = año
          #parametro por default

          self.kilometraje = 0
     
     def desplegar_info_auto (self):

          """Mostrar información formateada del auto"""

          info_auto = self.marca + " " + self.modelo + " " + str(self.año)

          print (info_auto.title())

     def mostrar_kilometros (self):

          print ("El kilometraje del auto es de: " + str(self.kilometraje) + " kilometros")

     #PODEMOS MODIFICAR UN PARAMETRO MEDIANTE OTROS METODOS 

     def actualizar_kilometraje(self, kilometraje):

          self.kilometraje = kilometraje

auto_1 = Auto("mercedes", "gt3", 2019)

auto_1.desplegar_info_auto()
auto_1.mostrar_kilometros()

#PODEMOS MODIFCAR LOS ATRIBUTOS DIRECTAMENTE

auto_1.kilometraje = 200
auto_1.mostrar_kilometros()
auto_1.actualizar_kilometraje(50)
auto_1.mostrar_kilometros()

     
     