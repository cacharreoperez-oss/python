import tkinter as tk
from tkinter import messagebox


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Tamaño de la ventana")

        # Barra de menú.
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)

        # Opciones del menú.
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(
            label="Cambiar tamaño",
            command=self.fijar_tamano
        )
        opciones1.add_command(
            label="Finalizar",
            command=self.finalizar
        )
        menubar1.add_cascade(label="Opciones", menu=opciones1)

        self.label1 = tk.Label(self.ventana1, text="Ancho:")
        self.label1.grid(column=0, row=0, padx=10, pady=5)

        self.entry_ancho = tk.Entry(self.ventana1, width=10)
        self.entry_ancho.grid(column=1, row=0, padx=10, pady=5)

        self.label2 = tk.Label(self.ventana1, text="Alto:")
        self.label2.grid(column=0, row=1, padx=10, pady=5)

        self.entry_alto = tk.Entry(self.ventana1, width=10)
        self.entry_alto.grid(column=1, row=1, padx=10, pady=5)

        self.ventana1.mainloop()

    def fijar_tamano(self):
        ancho = self.entry_ancho.get()
        alto = self.entry_alto.get()

        if ancho.isdigit() and alto.isdigit() and int(ancho) > 0 and int(alto) > 0:
            self.ventana1.geometry(ancho + "x" + alto)
        else:
            messagebox.showerror(
                "Datos incorrectos",
                "Escribe dos números enteros mayores que cero."
            )

    def finalizar(self):
        self.ventana1.destroy()


aplicacion1 = Aplicacion()