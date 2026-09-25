
import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.geometry("270x130")
        self.ventana1.title("Elige navegador")

        self.brave = tk.BooleanVar(value=False)
        self.chrome = tk.BooleanVar(value=False)
        self.firefox = tk.BooleanVar(value=False)
        self.edge = tk.BooleanVar(value=False)

        self.check1 = tk.Checkbutton(
            self.ventana1, text="Brave",
            variable=self.brave, command=self.poner_texto
        )
        self.check1.grid(column=0, row=0)

        self.check2 = tk.Checkbutton(
            self.ventana1, text="Chrome",
            variable=self.chrome, command=self.poner_texto
        )
        self.check2.grid(column=0, row=1)

        self.check3 = tk.Checkbutton(
            self.ventana1, text="Firefox",
            variable=self.firefox, command=self.poner_texto
        )
        self.check3.grid(column=0, row=2)

        self.check4 = tk.Checkbutton(
            self.ventana1, text="Edge",
            variable=self.edge, command=self.poner_texto
        )
        self.check4.grid(column=0, row=3)

        self.ventana1.mainloop()

    def poner_texto(self):
        seleccionados = []

        if self.brave.get():
            seleccionados.append("Brave")

        if self.chrome.get():
            seleccionados.append("Chrome")

        if self.firefox.get():
            seleccionados.append("Firefox")

        if self.edge.get():
            seleccionados.append("Edge")

        if seleccionados:
            self.ventana1.title(", ".join(seleccionados))
        else:
            self.ventana1.title("Elige navegador")


aplicacion1 = Aplicacion()