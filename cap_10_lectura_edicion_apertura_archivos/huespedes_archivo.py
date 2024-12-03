from datetime import *

#LIBRERIA PARA IMPORTAR FECHA.

huespedes = [] #LISTA QUE ALBERGA LOS NOMBRES DE LOS HUESPEDES

def agregarHuesped ():

     '''AGREGA HUESPEDES A UNA LISTA'''
        
     activador = True 

     while activador:

          print ("***BIENVENIDO AL PROGRAMA DE REGISTRO DE HUESPEDES.")

          instrucciones = "Por favor, escriba su nombre completo:"

          nombre_huesped = input(instrucciones)

          huespedes.append(nombre_huesped) #AGREGO A LA LISTA LOS HUESPEDES AGREGADOS

          continuar = input ("¿Desea agregar otro huesped?...s/n")

          if continuar == "n":

               print ("Registro finalizado.")
               activador = False


def mandarSaludo():
        
        '''MANDA UN SALUDO A CADA HUESPED AGREGADO'''
        
        for huesped in huespedes:
                
                print ("Gracias por visitarnos: " + huesped + ".")

def guardarRegistro():
        
        '''REGISTRA LOS HUESPEDES EN UN ARCHIVO DE TEXTO Y GUARDA LA FECHA DE REGISTRO.'''
        
        ruta_archivo_registro = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/huespedes.txt"

        with open (ruta_archivo_registro, 'a')as file_object:
                
                for huesped in huespedes:
                        
                        file_object.write("\n" + "Visita registrada de: " + huesped + " en la fecha del: " + str(datetime.now()) + "\n") 

#MANDAMOS A LLAMAR LOS METODOS O FUNCIONES PERTINENTES.

agregarHuesped()
mandarSaludo()
guardarRegistro()
                



     