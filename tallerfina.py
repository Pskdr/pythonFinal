import tkinter as tk
from tkinter import Toplevel

def abrir_ventana(titulo):
    nueva_ventana = Toplevel(root)
    nueva_ventana.anchor('center')
    nueva_ventana.title(titulo)
    etiqueta = tk.Label(nueva_ventana, text=titulo)
    etiqueta.pack(padx=200, pady=200)

root = tk.Tk()
root.title("Menú Principal")
root.anchor('center')

etiqueta_principal = tk.Label(root, text="Elija la ecuación que desea realizar:")
etiqueta_principal.pack(pady=10)

botones = ["Método de Taylor", "Interpolación", "Gráficas", "Ceros", "Integración"]

for boton in botones:
    b = tk.Button(root, text=boton, command=lambda t=boton: abrir_ventana(t))
    b.pack(pady=5)

root.mainloop()
