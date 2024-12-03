'''

dentro del metodo open(file, 'w, r, a')

w = escritura
r = lectura
a = append
r+ = lectura mas escritura

POR DEFECTO PYTHON ABRE LOS ARCHIVOS EN MODO LECTURA

'''

archivo = "/media/luis-alberto/1TB LUIS/Desarrollo/Python Workspace/cap_10/archivos_lectura_python/mensaje_2.txt"



with open (archivo, 'r+') as file_object: #INDICAMOS EL MODO ESCRITURA Y LECTURA CON EL SEGUNDO PARAMETRO


     #USAMOS EL METODO.WRITE("MODIFICACION AL TEXTO O ARCHIVO")
     #PODEMOS ESCRIBIR MULTIPLES LINEAS 

     file_object.write("Modificación mediante Python y el modo escritura de archivos.")
     file_object.write("\nSegunda modificación mediante Python.")
     file_object.write("\nTercera modificación mediante Python.")
     
