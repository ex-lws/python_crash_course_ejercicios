#Borrar elementos de una lista, borrar pastrami de la lista original

ordenes_sandwiches = ["pollo", "salami","pastrami", "lechuga con mostasa", "lasaña", "carne molida", "pastrami", "pastrami"]
print ("Ordenes actuales...", ordenes_sandwiches)

ordenes_sandwiches_terminadas = []

while "pastrami" in ordenes_sandwiches:
  ordenes_sandwiches.remove("pastrami")

while ordenes_sandwiches:

  orden_terminada = ordenes_sandwiches.pop()
  ordenes_sandwiches_terminadas.append(orden_terminada)

print ("Ordenes finalizadas de sanwiches...")

mostrar = input("¿Desea constultar las ordenes finalizadas? s/n")

if mostrar == "s":

  print (ordenes_sandwiches_terminadas)


