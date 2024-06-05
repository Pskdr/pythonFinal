import tkinter as tk
from tkinter import Toplevel
from metodo_de_taylor import abrir_metodo_de_taylor
from interpolacion import abrir_interpolacion
from graficas import abrir_graficas
from ceros import abrir_ceros
from integracion import abrir_integracion

def abrir_ventana(titulo):
    nueva_ventana = Toplevel(root)
    nueva_ventana.anchor('center')
    nueva_ventana.title(titulo)
    etiqueta = tk.Label(nueva_ventana, text=titulo)
    etiqueta.pack(padx=200, pady=200)

root = tk.Tk()
root.anchor('center')
root.title("Menú Principal")

etiqueta_principal = tk.Label(root, text="Elija la ecuación que desea realizar:")
etiqueta_principal.pack(pady=10)

botones = [
    ("Método de Taylor", abrir_metodo_de_taylor),
    ("Interpolación", abrir_interpolacion),
    ("Gráficas", abrir_graficas),
    ("Ceros", abrir_ceros),
    ("Integración", abrir_integracion),
]

for (texto, funcion) in botones:
    b = tk.Button(root, text=texto, command=lambda f=funcion: abrir_ventana(f))
    b.pack(pady=10,padx=100)

root.mainloop()
