import tkinter as tk
from tkinter import Toplevel
from metodo_de_taylor import abrir_metodo_de_taylor
from sistemas_ecuaciones_lineales import abrri_sistemas_ecuaciones_lineales
from ecuaciones_diferenciales import abrir_ecuaciones_diferenciales
from ceros import abrir_ceros
from interpolacion import abrir_interpolacion

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
    ("Serie de taylor", abrir_metodo_de_taylor),
    ("Ceros de funciones", abrir_ceros),
    ("Sistemas de Ecuaciones Lineales", abrri_sistemas_ecuaciones_lineales),
    ("Interpolación y ajuste", abrir_interpolacion),
    ("Ecuaciones diferenciales", abrir_ecuaciones_diferenciales),
]

for (texto, funcion) in botones:
    b = tk.Button(root, text=texto, command=lambda f=funcion: abrir_ventana(f))
    b.pack(pady=10,padx=100)

root.mainloop()
