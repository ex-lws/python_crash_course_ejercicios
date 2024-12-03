#Ordenes de sandwiches

ordenes_sandwiches = ["pollo", "salami", "lechuga con mostasa", "lasaña", "carne molida"]
print ("Ordenes actuales...", ordenes_sandwiches)

ordenes_sandwiches_terminadas = []

while ordenes_sandwiches:
  orden_terminada = ordenes_sandwiches.pop()
  ordenes_sandwiches_terminadas.append(orden_terminada)

print ("Ordenes finalizadas de sanwiches...")

mostrar = input("¿Desea constultar las ordenes finalizadas? s/n")

if mostrar == "s":

  print (ordenes_sandwiches_terminadas)

