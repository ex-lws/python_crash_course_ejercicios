#PODEMOS USAR DENTRO DE LAS FUNCIONES LOS BUCLES TANTO FOR COMO WHILE
#EL BUCLE WHILE REQUIERE DE UN ACTIVADOR PARA ENTRAR Y DICHO ACTIVADOR DEBE CAMBIAR PARA SALIR DEL BUCLE.

def agregar_usuarios(nombre_usuario):

    while True: 

        print ('Bienvenido al programa de registro')

        usuarios = []

        print ('Usuario agregado con exito')
        usuarios.append(nombre_usuario)

        instrucciones = 'Escriba quit para salir en cualquier momento y mostrar los usuarios agregados'

        activador = input(instrucciones)

        if activador == "quit":

            print ('Saliendo del programa...')
            print (usuarios)
            break

#AGREGO TRES USUARIOS MEDIANTE LA FUNCION A UNA LISTA.

agregar_usuarios('luis')
agregar_usuarios('fernanda')
agregar_usuarios('devian')