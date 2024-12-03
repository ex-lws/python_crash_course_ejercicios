#PODEMOS TRABAJAR CON LISTAS EN EL LUGAR DE LOS PARAMETROS DE UNA FUNCION Y MODIFICARLAS DESDE LA PROPIA FUNCION.


#LOS PARAMETROS SON DOS LISTAS POR AHORA VARIAS...
#PERO QUE CUANDO SE INSTANCIEN PUEDEN LLENARSE DE ELEMENTOS...

def terminarPedidos(pedidos_pendientes, pedidos_completados):

  while pedidos_pendientes:
    pedido_actual = pedidos_pendientes.pop()
    print ("Añandiendo pedido:" + pedido_actual.title() + " a pedidos completados")

    pedidos_completados.append(pedido_actual)

def mostrarPedidosCompletados(pedidos_completados):
    print ("Los siguientes pedidos han sido terminados...")
    for pedido_completado in pedidos_completados:
      print (pedido_completado.title())
    print ("lista de pedidos completados: " + str(pedidos_completados))

pedidos_incompletos_marzo = ["Funda color negro edición Marvel", "Funda color rojo edición F1", "Funda color rosa edición DC Comics"]
pedidos_completos_marzo = []

terminarPedidos(pedidos_incompletos_marzo, pedidos_completos_marzo)
mostrarPedidosCompletados(pedidos_completos_marzo)

#LISTA QUE NO TENIA ELEMENTOS AHORA SE LLENO CON LOS ELEMENTOS DE LA LISTA PASADA.
print (pedidos_completos_marzo)