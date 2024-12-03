import tkinter
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.title("Multiplicadora")
ventana.geometry("400x400")

def multiplciar():

     valor1 = float(entrada1.get())
     valor2 = float(entrada2.get())
     resultado = valor1 * valor2

     mostrar_resultado = "Resultado obtenido: " + str(resultado)
     
     messagebox.showinfo("Resultado", mostrar_resultado)

etiqueta1 = tkinter.Label(ventana, text = "Introducir primer valor")
etiqueta1.pack()
entrada1 = tkinter.Entry()
entrada1.pack()

etiqueta2 = tkinter.Label(ventana, text = "Introducir segundo valor")
etiqueta2.pack()
entrada2 = tkinter.Entry()
entrada2.pack()

boton_calcular = tkinter.Button(ventana, text = "Calcular", command=multiplciar)
boton_calcular.pack()

ventana.mainloop()