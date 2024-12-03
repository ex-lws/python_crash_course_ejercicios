import tkinter

ventana_2 = tkinter.Tk()
ventana_2.title("Widgets")

#.grid(row=0, column=0) indica la posicion de los elementos.

tkinter.Label(ventana_2, text= "Hola a todos").grid(row=0, column=0)
tkinter.Entry(ventana_2).grid(row=0, column=1)
tkinter.Button(ventana_2, text="Subir datos").grid(row=1, column=1)

ventana_2.mainloop()