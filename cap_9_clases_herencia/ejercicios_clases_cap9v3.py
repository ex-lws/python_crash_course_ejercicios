#Heredar de restaurante y crear una subclase llamada puesto de helados.

class Restaurante():

    def __init__(self, nombre_restaurante, tipo_cocina):

        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        #Valor por defecto de clientes atendidos
        self.cantidad_clientes_atendidos = 0

    def describir_restaurante(self):

        print ('El restaurante: ' + self.nombre_restaurante.title() + ' es de alta cocina.')
        print ('Su especialidad son todos los platillos del tipo de cocina: ' + self.tipo_cocina.title())

    def abrir_restaurante(self):

        print ('El restaruante: ' + self.nombre_restaurante.title() + ' de cocina: ' + self.tipo_cocina.title() + ' ha abierto sus puertas.')

    def asignar_clientes_atendidos(self, cantidad):

        self.cantidad_clientes_atendidos = cantidad

class Puesto_helados(Restaurante):
    
     def __init__(self, nombre_restaurante, tipo_cocina):
        
          super().__init__(nombre_restaurante, tipo_cocina)

          self.sabores = ["vainilla", "napolitano", "chocolate", "queso y frambuesa"]
        
     def mostrarSabores(self):
        
          for sabor in self.sabores:
               print ("Tenemos helados sabor: " + sabor)

#Instancias de la clase hija

helado_1 = Puesto_helados("Amore pizza", "italiana")
helado_1.mostrarSabores()

#Heredar de la clase usuario y crear una subclase que se llame admin

class Usuario():

    def __init__(self, nombres, edad, estudios, correo):

        self.nombres = nombres
        self.edad = edad
        self.estudios = estudios
        self.correo = correo
        self.intentos_inicio_sesion = 0

    def describir_usuario(self):

        print ('El usuario: ' + self.nombres.title() + ' tiene una edad de: ' + str(self.edad))
        print ('Tiene como estudios: '+ self.estudios.title())
        print ('Su forma de contacto es mediante el correo personal: ' + self.correo)

    def saludar_usuario(self):

        print ('Bienvenido a la empresa: ' + self.nombres.title())

    def incrementar_intentos_inicio_sesion(self, intentos):

        intentos = int(self.intentos_inicio_sesion) + 1
        print (intentos)


    def resetar_intentos_inicio_sesion(self, intentos):

        intentos = 0
        self.intentos_inicio_sesion = intentos
        print (intentos)

class Administrador (Usuario):

    def __init__(self, nombres, edad, estudios, correo):

        super().__init__(nombres, edad, estudios, correo)

        self.privilegios = ["Puede añadir datos", "Puede borrar datos", "Puede ser un usuario"]

    
    def mostrar_permisos(self):

        for privilegio in self.privilegios:

            print (privilegio.upper())

admin_1 = Administrador("luis alberto", 22, "ingeniero de software", "leroyb@gmail.com")
admin_1.mostrar_permisos()
    
