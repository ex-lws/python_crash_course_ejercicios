'''
Probar el codigo es parte fundamental a la hora de programar, es util para encontrar errores antes de que el usuario los encuentre por si solos.

'''

def formatearNombre (nombres, apellido_paterno, apellido_materno):

     nombre_completo = nombres + apellido_paterno + apellido_materno
     return nombre_completo.title()

formatearNombre('Luis Alberto', 'reyes', ' cruz')

