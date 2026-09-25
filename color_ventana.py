import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cambiar color de fondo")
        self.ventana.resizable(False, False)

        self.contenido = tk.Frame(self.ventana, padx=15, pady=15)
        self.contenido.grid(column=0, row=0)

        self.color = tk.StringVar(value="red")

        self.radio_rojo = tk.Radiobutton(
            self.contenido, text="Rojo",
            variable=self.color, value="red"
        )
        self.radio_rojo.grid(column=0, row=0, sticky="w")

        self.radio_verde = tk.Radiobutton(
            self.contenido, text="Verde",
            variable=self.color, value="green"
        )
        self.radio_verde.grid(column=0, row=1, sticky="w")

        self.radio_azul = tk.Radiobutton(
            self.contenido, text="Azul",
            variable=self.color, value="blue"
        )
        self.radio_azul.grid(column=0, row=2, sticky="w")


        self.radio_negro = tk.Radiobutton(
            self.contenido, text="Negro",
            variable=self.color, value="black"
        )
        self.radio_negro.grid(column=0, row=3, sticky="w")        

        self.boton = tk.Button(
            self.contenido, text="Cambiar color",
            command=self.cambiar_color
        )
        self.boton.grid(column=0, row=4, pady=(10, 0))

        self.ventana.mainloop()

    def cambiar_color(self):
        color_elegido = self.color.get()
        self.ventana.configure(bg=color_elegido)
        self.contenido.configure(bg=color_elegido)

        # Evita que quede el fondo anterior detrás de las opciones.
        self.radio_rojo.configure(bg=color_elegido)
        self.radio_verde.configure(bg=color_elegido)
        self.radio_azul.configure(bg=color_elegido)
        self.radio_negro.configure(bg=color_elegido)        


aplicacion = Aplicacion()