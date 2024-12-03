#CLASE PADRE


class Empleado():

     def __init__(self, nombre, puesto, salario):

          '''
          CLASE EMPLEADO
          '''


          self.nombre = nombre 
          self.puesto = puesto
          self.salario = float(salario)

     def mostrarInformacion(self):

          '''
          IMPRIME LOS DATOS RELEVATES DEL EMPLEADO
          ''' 

          datos = "Nombre del empleado: " + self.nombre.title() + "." + "\nPuesto en la empresa: " + self.puesto.title() + "." + "\nSalario actual: " + str(self.salario)


          print ("***IMPRIMENDO DATOS DEL EMPLEADO***")
          print (datos)

     def amuentarSalario(self):

          '''
          AUMENTA EL SALARIO DEL EMPLEADO CON LOS BONOS DE HORA EXTRAS
          '''

          bono_por_hora_extra = 200.25

          cantidad_horas_extra = int(input("Escriba la cantidad de horas extra trabajadas..."))

          bono = (cantidad_horas_extra * bono_por_hora_extra)

          salario_final = self.salario + bono

          print ("Al haber trabajado: " + str(cantidad_horas_extra) + " de horas." + " Su salario es de: " + str(salario_final))
          print ("Su bono es de:" + str(bono))


#INSANTCIAR 

empleado_1 = Empleado("luis alberto reyes cruz", "gerente", 15250)
empleado_1.amuentarSalario()


class Desarrolador (Empleado):

     def __init__ (self, nombre, puesto, salario):

          super().__init__(nombre, puesto, salario)

          self.numero_proyectos = 5

     def mostarProyectos(self):


          print ("La cantidad de proyecto del desarrollador es: " + str(self.numero_proyectos))
          

Desarrolador_1 = Desarrolador("Jaime Leibz", "desarrollador", 7650)
Desarrolador_1.mostrarInformacion()
Desarrolador_1.amuentarSalario()
Desarrolador_1.mostarProyectos()