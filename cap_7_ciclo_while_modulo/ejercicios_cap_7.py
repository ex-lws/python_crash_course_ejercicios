#toppings de pizzas

print ("Bienvenido al programa de armado de pizzas.")

activador = input('Escriba "enter" si desea entrar al programa o "quit" para terminarlo.')
lista_toppings = []

while activador == "enter":

  toppings = input("Ingresa los toppings a agregar a su pizza")
  lista_toppings.append(toppings)
  print ("¿Desea continuar agregando toppings a su pizza?")
  continuar = input ("s/n")

  if continuar == "n":
    print ("Orden finalizada...")
    break

print ("Su pizza está lista, los ingredientes son: ", lista_toppings)


