from tkinter import *

def miFuncion():
    print("Este mensaje es del boton.")

ventana = Tk()
ventana.title("Hola Mundo")
ventana.geometry("400x280")

lbl = Label(ventana, text = "Este es un label")
lbl.config(fg="red", bg="blue")
lbl.pack()

btn = Button(ventana, text="Presionar", command = miFuncion)
btn.config(fg="yellow", bg="gray")
btn.pack()


ventana.mainloop()