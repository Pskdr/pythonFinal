import tkinter as tk
from tkinter import Toplevel

def abrir_ceros():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Ceros")
    etiqueta = tk.Label(nueva_ventana, text="Ceros")
    etiqueta.pack(padx=20, pady=20)
