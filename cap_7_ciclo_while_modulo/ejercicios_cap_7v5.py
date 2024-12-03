#Lugar al que quieres ir a vacacionar

solicitudes_hospitales = {}

mensaje = ("Bienvenido al programa de solicitud de hospitales.")

activador = input ("\n\tEscriba 'enter' para ingresar al programa o 'quit' para salir del programa.")

if activador == "enter":

  bucle = True

  while bucle:

    numero_cuenta = int(input("Escriba su número de cuenta."))
    hosiptal_solicitado = input("Escriba el nombre del hospital que va a solicitar.")

    solicitudes_hospitales[numero_cuenta] = hosiptal_solicitado

    continuar = input ("¿Desea hacer otro registro? s/n")

    if continuar == "n":

      bucle = False
      print ("¡Registro realziado con éxito!")

print ("Solicitud registrada: ", solicitudes_hospitales)