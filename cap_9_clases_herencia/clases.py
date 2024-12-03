#Una clase es una serie de caracteristicas sobre algo en concreto. 
#Las clases se pueden instanciar y permiten heredar sus atributos, parametros y metodos en cualquier parte del 
#codigo a fin de modulacion.

#Una regla de programacion es que las clases por covnecion incian con letra mayuscula.
#Seguida de una breve descripcion de lo que la clase hace...


class Perro():

    """Clase perro que puede instanciar a otros perros. El nivel de abstaccion puede ser; animal."""

    def __init__(self, nombre, edad):

        #Init incializa los atributos de la clase Perro, self va primero que todos los demas parametros.
        #Incializamos los atributos con self y los pasamos a variables

        #Se le llama constructor.

        '''sinaxis del self para constructor'''

        #self.parametro = parametro
        #SE PUEDEN INCLUIR PARAMETROS UNICOS AQUI EN EL CASO DE LAS CLASES HIJAS.

        self.nombre = nombre
        self.edad = edad

    #Creo diversos metodos que involucran los atributos inicialziados con __init__

    def sentarse(self):

        print ('El perro:' + self.nombre.title() + ' es capaz de poder sentarse.')

    def rodar(self):

        print ('El perro: '+ self.nombre.title() + ' es capaz de poder rodar por el suelo.')

#Instanciamos la clase perro

perro_1 = Perro('Nality Bality', 3) #Pasamos valores a los atrubitos de la clase perro

#Accediendo a metodos 

perro_1.sentarse()
perro_1.rodar()

#Realizamos una segunda instancia

perro_2 = Perro('dogen vogen', 5) #Pasamos valores a los atributos

#Accediendo a metodos = instancia 2

perro_2.sentarse()
perro_2.rodar()

#Accediendo a atributos individuales de las diferentes instancias.

print (perro_1.nombre)
print (perro_2.nombre)
print (perro_1.edad)
print (perro_2.edad)

'''

Una instancia es básicamente poderle pasar los elementos necesarios a la clase para poder trabajr con ella y sus metodos.
Las clases por regular son para modulacion y reutilizacion de codigo...

'''    
