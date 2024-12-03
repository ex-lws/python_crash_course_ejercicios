#Es importante que mediante el uso de modulos vayamos seccionando las partes del codigo en clases separadas
#La clase padre, hija en diferentes archivos.

#Esta es una clase padre.

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