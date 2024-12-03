'''

MANEJO DE ERROR EN CASO DE ENCONTRAR UN ARCHIVO

'''

archivo = "mensaje_2.txt"

try:

     with open (archivo, 'r') as file_object:

               cotenido = file_object.read(archivo)
               print (cotenido)

except FileNotFoundError: 
        
        print ("El archivo: " + archivo + " no existe en el directorio especificado.")

'''

ES IMPORTANTE TOMAR EN CUENTA QUE DEBEMOS DE BUSCAR DONDE PUEDE ESTAR EL ERROR
Y PODER CAPTURARLO, EVITAR QUE SUCEDA Y SI NO HAY DE OTRA MANDAR UN MENSAJE QUE EL USUARIO PUEDA INTERPRETAR 

'''
