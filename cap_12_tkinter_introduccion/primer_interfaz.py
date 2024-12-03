import tkinter #Permite poder desarrollar GUIS en Python

def imprimir_saludo():

     etiqueta_bienvenida.config(text = "Muy buenas tardes, amigo") #Actualiza la etiqueta "Bienvenido"

ventana = tkinter.Tk() #Creamos una ventana nueva

ventana.title("Mi primer programa en Tkinter") #Le agregamos un titulo a la ventana

ventana.geometry("400x400") #Definimos un tamaño para la ventana

etiqueta_bienvenida = tkinter.Label(ventana, text = "Bienvenido.")#Agregamos una etiqueta.
etiqueta_bienvenida.pack() #Agrega el elemento en la posicion superior de la ventana.

boton_mostrar_saludo = tkinter.Button(ventana, text = "Mostrar saludo", command=imprimir_saludo)
boton_mostrar_saludo.pack()

ventana.mainloop() #Permite ejecutar la ventana en tiempo real


