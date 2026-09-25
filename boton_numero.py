import tkinter as tk
import sys
class Aplicacion:
    def __init__(self):
        self.numero = "" 
        self.ventana = tk.Tk()
        #self.ventana.geometry("170x90")
        self.ventana.resizable(False, False)
        self.ventana.title("Ejercicio 2")
        self.label1 = tk.Label(self.ventana, text="Valor del boton")
        self.label1.grid(column=0, row=1, columnspan=5)
        self.boton1 = tk.Button(self.ventana, text="1", command=lambda: self.valor("1")).grid(column=0, row=4)
        self.boton2 = tk.Button(self.ventana, text="2", command=lambda: self.valor("2")).grid(column=1, row=4)
        self.boton3 = tk.Button(self.ventana, text="3", command=lambda: self.valor("3")).grid(column=2, row=4)
        self.boton4 = tk.Button(self.ventana, text="4", command=lambda: self.valor("4")).grid(column=3, row=4)
        self.boton5 = tk.Button(self.ventana, text="5", command=lambda: self.valor("5")).grid(column=4, row=4)
        self.ventana.mainloop()
    def valor(self, num=0):
        self.numero= self.numero + num
        self.label1.config(text=f"Valor del botón {self.numero }")
aplicacion = Aplicacion()