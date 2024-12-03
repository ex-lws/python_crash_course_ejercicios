import tkinter
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.title("Ejercicio 2")
ventana.geometry("400x200")

def enviar_informacion():

     nombre_usuario = entrada_1.get() #.get obtiene los valores de las entradas y los manda a una variable
     correo_usuario = entrada_2.get()

     mensaje = "Su nombre es :" + nombre_usuario + " y su correo es: " + correo_usuario

     messagebox.showinfo("Información del Formulario", mensaje)#Muetsra un mensaje emergente y puede imprimir variable.

etiqueta_1 = tkinter.Label(ventana, text = "Nombre")
etiqueta_1.pack()

entrada_1 = tkinter.Entry(ventana)
entrada_1.pack()

etiqueta_2 = tkinter.Label(ventana, text = "Correo electronico")
etiqueta_2.pack()

entrada_2 = tkinter.Entry(ventana)
entrada_2.pack()

boton_1 = tkinter.Button(ventana, text = "Insertar", command= enviar_informacion)
boton_1.pack()

ventana.mainloop()