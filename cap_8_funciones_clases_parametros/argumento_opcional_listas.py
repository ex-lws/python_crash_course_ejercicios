#PODEMOS COLOCAR EN LA DEFINICION DE LA FUNCION, PARAMETROS OPCIONALES...

#LOS PARAMETROS OPCIONALES SON AQUELLOS QUE SE LES ASIGNA UN ESPACIO EN BLANCO...

#AL HACER ESTO NO ES NECESARIO QUE CUANDO SE HAGA UNA INSTANCIA DEL METODO SE COLOQUEN

def almacenarDatosEmpleado (nombre_empelado, cargo, correo_electronico, genero = '' ):

    almacen_datos = [nombre_empelado, cargo, correo_electronico, genero]

    if 'edad' in almacen_datos:

        print (almacen_datos)
    else:

        return almacen_datos
    
empleado1 = almacenarDatosEmpleado('Luis', 'supervisor', 'guichin99@gmail.com', 'masculino')
print (empleado1)

empelado2_sin_genero = almacenarDatosEmpleado('Xavi', 'quimico', 'leroyb@gmail.com')
print (empelado2_sin_genero)