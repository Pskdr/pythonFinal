import tkinter as tk
from tkinter import Toplevel

def abrir_interpolacion():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Integración")
    etiqueta = tk.Label(nueva_ventana, text="Integración")
    etiqueta.pack(padx=20, pady=20)
