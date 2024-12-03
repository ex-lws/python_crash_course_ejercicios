#LAS FUNCIONES PUEDE RETORNAR DICCIONARIOS SI ASI SE QUIERE
#LOS PARAMETROS SE ALMACENAN EN LUGAR DE LOS VALUES, ES DECIR SE HACEN PAR CON LAS KEYS.

def almacenar_pc (marca_pc, precio_pc, sistema_operativo_pc = ''): #PODEMOS OBVIAR EL PARAMETRO DE SISTEMA OPERATIVO

    almacen_pc = {'marca': marca_pc, 'precio' : precio_pc}

    if sistema_operativo_pc: #EN CASO DE QUE SE INSTANCIARA DICHO PARAMETRO, SE AGREGA AL DICCIONARIO
        almacenar_pc ['os'] = sistema_operativo_pc

    return almacenar_pc

pc_1 = ('asus', 250000, 'windows')
pc_2 = ('corsair', 17500)
print (pc_1)
print (pc_2)