#Programa de asignación de precio a diversos boletos de cine utilizando continue y quit

mensaje_bienvenida = "Bienvenido al programa de asignación de boletos."

instrucciones_usuario = '\n\tEscriba "enter" para acceder o "quit" para finalizar su orden.'

activador = input(instrucciones_usuario)

costo_total_boletos = []

while activador == "enter":

  edad = int(input ("Escriba por favor, las edades o la edad del asistente."))

  if edad <3:
    costo_total_boletos.append(0)

  elif edad >=3 and edad <=12:
    costo_total_boletos.append(10)

  elif edad >12:
    costo_total_boletos.append(15)

  continuar = input("¿Desea agregar más asistentes? s/n")

  if continuar == "s":
    continue

  elif continuar == "n":
    print ("Orden finalizada con exito.")
    break

print ("'\n\tEl costo total es de:", sum(costo_total_boletos), " pague en ventanilla.")
