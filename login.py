'''

Ingresar el nombre de usuario y clave en controles de tipo Entry. 
Si se ingresa las cadena (usuario: juan, clave="abc123") 
luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".
Para mostrar '*' cuando se ingresa la clave debemos pasar en el parámetro 'show' el caracter a mostrar:

'''

import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.resizable(False, False)

        self.contenido = tk.Frame(self.ventana, padx=15, pady=15)
        self.contenido.grid(column=0, row=0)

        self.label_usuario = tk.Label(self.contenido, text="Usuario:")
        self.label_usuario.grid(column=0, row=0)

        self.entry_usuario = tk.Entry(self.contenido)
        self.entry_usuario.grid(column=1, row=0,pady=10)

        self.label_clave = tk.Label(self.contenido, text="Clave:")
        self.label_clave.grid(column=0, row=1)

        self.entry_clave = tk.Entry(self.contenido, show="*")
        self.entry_clave.grid(column=1, row=1)

        self.boton = tk.Button(self.contenido, text="Ingresar", command=self.comprobar)
        self.boton.grid(column=0, row=2, columnspan=2, pady=15)

        self.ventana.mainloop()

    def comprobar(self):
        usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()

        if usuario == "juan" and clave == "abc123":
            self.ventana.title("Correcto")
        else:
            self.ventana.title("Incorrecto")


aplicacion = Aplicacion()