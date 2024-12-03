#Introducir informacion mediante un while a un diccionario.

print ("Bienvenido al sistema de almacenamiento de contaseñas.")

contraseñas_almaceadas = {}

activador = input("Por favor, escriba 'enter' para empeza a agregar contraseñas o 'quit' para salir del programa.")

while activador == "enter":

  nombre_contraseña = input("Ingrese el nombre de su contraseña para identificarla")
  contraseña = input("Por favor escriba su contraseña")

  contraseñas_almaceadas[nombre_contraseña] = contraseña #Almacenar key and value al diccioario.

  seguir = input ("Quiere agreagar otra contraseña? s/n")

  if seguir == "n":

    print ("Saliendo del programa.")
    break

mostrar_contraseñas = input ("¿Desea consultar sus contraseñas almaceadas a fin de consulta? s/n")

if mostrar_contraseñas == "s":

  print (contraseñas_almaceadas)

else:
  print ("Gracias por usar el programa.")








