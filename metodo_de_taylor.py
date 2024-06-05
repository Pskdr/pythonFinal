import tkinter as tk
from tkinter import Toplevel

def abrir_metodo_de_taylor():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Método de Taylor")
    etiqueta = tk.Label(nueva_ventana, text="Método de Taylor")
    etiqueta.pack(padx=20, pady=20)
