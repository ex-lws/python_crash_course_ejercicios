#Restaurantes

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


restaurante_1 = Restaurante('el amore pizza', 'italiana')
restaurante_1.describir_restaurante()
restaurante_1.abrir_restaurante()

restaurante_2 = Restaurante('la patronad', 'mexicana')
restaurante_2.describir_restaurante()

restaurante_3 = Restaurante('don porfirio', 'cocteleria')
restaurante_3.describir_restaurante()

restaurante_4 = Restaurante('madre mediterranea', 'espanola')
restaurante_4.describir_restaurante()
restaurante_4.asignar_clientes_atendidos(250)

print (restaurante_4.cantidad_clientes_atendidos)

#Usuarios

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
    
        

usuario_1 = Usuario('luis alberto', 18, 'ingeniero en computacion', 'guchin@gmail.com')
usuario_1.describir_usuario()
usuario_1.saludar_usuario()
print (usuario_1.intentos_inicio_sesion)
usuario_1.incrementar_intentos_inicio_sesion(0)
usuario_1.resetar_intentos_inicio_sesion(1)