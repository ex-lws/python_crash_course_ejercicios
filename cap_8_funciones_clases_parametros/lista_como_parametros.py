#PODEMOS USAR UNA LISTA DE VARIOS ELEMENTOS Y TRABAJAR CON ELLOS

#COMO PODEMOS VER EL PARAMETRO ES UNA LISTA VACIA, EN LA QUE EL FOR RECORRERA LOS ELELEMTOS AGREGADOS 
#EN agregar_3_usrs

def argegar_usuarios(nombres_usrs):

    for nombre_usr in nombres_usrs: #POR CADA ELEMENTO AGREGADO EN EL PARAMETRO...

        print ('Bienvenido al sistema: ' + nombre_usr)

agregar_3_usrs = ['randal', 'hofeel', 'dreuss']

argegar_usuarios(agregar_3_usrs)

agregar_2_usrs = ['Ferchus', 'Ange', 'Guichin']

argegar_usuarios(agregar_2_usrs)


'''

Hay que tener en cuenta que los parametros o argumentos son parte fundamental de los metodos...
Estos pueden tomar cualquier tipo de dato o variable para cumplir el proposito de la función.

'''