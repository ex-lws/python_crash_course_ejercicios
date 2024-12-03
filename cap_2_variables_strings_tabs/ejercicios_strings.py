#Ejercicios con strings del capitulo 2.

nombre_persona = "Luis Alberto"

print ("Hola, querido " + nombre_persona + ", ¿quieres aprender Python en dia de hoy?")

print (nombre_persona.lower()) #Convierete a minusculas
print (nombre_persona.upper()) #Convierte a mayusculas 
print (nombre_persona.title()) #El mas adecuado para nombres de obras y personas

#Comillas dobles dentro de comillas simples.

frase_celebre = 'Octavio Paz, dijo alguna vez: "Yo soy tu lejania."'

print (frase_celebre)

#Strings a variables.

intelectual = "octavio paz" #Mandamos al autor a una variable

frase = intelectual.title() + ', dijo alguna vez: "Yo soy tu lejania."'

print (frase) #Mandamos la frease a otra variable y concatenamos

autor = " edgar Allan Poe "

#usamos saltos de linea, tabs, titulo y borrado de espacios en blanco

print ("Un autor que escribe terror es:" + "\n\t" + autor.strip().title())
print ("Un autor que escribe terror es:" + "\n\t" + autor.lstrip().title())
print ("Un autor que escribe terror es:" + "\n\t" + autor.rstrip().title())






