#EL METODO SPLIT LO QUE HACE ES DIVIDIR EN PALABRAS UN STRING

texto = "Hola, amigos de Python. Este es un mensaje..."

print ("Texto integro: " + texto)

#MANDAMOS TODAS LAS PALABRAS SEPARADAS EN EL STRING A UNA NUEVA VARIABLE

#.split() SEPARA TODAS LAS PALABRAS EN EL STTRING Y LAS MANDA A UNA LISTA

palabras = texto.split()

numero_palabras = len(palabras)

#PARA SABER EL NUMERO DE PALABRAS USAMOS UN LEN

print (palabras)
print (numero_palabras)