import tkinter

def mensaje_boton():

     etiqueta1.config(text = "Botón 1 presionado.")

def mensaje_boton_2():
     etiqueta2.config(text = "Botón 2 presionado.")

def mensaje_boton_3():
     etiqueta3.config(text = "Botón 3 presionado.")

ventana_2 = tkinter.Tk()
ventana_2.title("Ejercicio 1")

ventana_2.geometry("400x300")

etiqueta1 = tkinter.Label(ventana_2, text = "Botón 1")
etiqueta1.pack()

boton1 = tkinter.Button(ventana_2, text = "presioname", command= mensaje_boton)
boton1.pack()

etiqueta2 = tkinter.Label(ventana_2, text = "Botón 2")
etiqueta2.pack()

boton2 = tkinter.Button(ventana_2, text = "Presioname", command = mensaje_boton_2)
boton2.pack()

etiqueta3 = tkinter.Label(ventana_2, text = "Botón 3")
etiqueta3.pack()

boton3 = tkinter.Button(ventana_2, text="Presioname", command= mensaje_boton_3)
boton3.pack()

ventana_2.mainloop()