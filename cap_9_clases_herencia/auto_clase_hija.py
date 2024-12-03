#Una forma de poder importar a la clase padre es...

#from tituloArchivo = nombreClase

#import Auto, que es la clase que nos interesa y que contiene todos los metodos y atributos que necesitamos

from clase_auto import Auto

#Si tuvieramos más clases o metodos, podríamos importarlos todos con...

from clase_auto import * 

#Instanciamos la clase importada...

auto_1 = Auto("audi", "m3", 2017)
auto_1.desplegar_info_auto()