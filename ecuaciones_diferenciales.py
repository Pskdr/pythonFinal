import tkinter as tk
from tkinter import Toplevel

def abrir_ecuaciones_diferenciales():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Gráficas")
    etiqueta = tk.Label(nueva_ventana, text="Gráficas")
    etiqueta.pack(padx=20, pady=20)
