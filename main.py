import tkinter as tk
from metodo_de_taylor import abrir_metodo_de_taylor
from sistemas_ecuaciones_lineales import abrir_sistemas_ecuaciones
from ecuaciones_diferenciales import abrir_ecuaciones_diferenciales
from ceros import abrir_ceros
from interpolacion import abrir_interpolacion

root = tk.Tk()
root.title("Menú Principal")

etiqueta_principal = tk.Label(root, text="Elija la ecuación que desea realizar:")
etiqueta_principal.pack(pady=10)

boton_serie_de_Taylor = tk.Button(root, text="Serie de Taylor", command=abrir_metodo_de_taylor, width=25, height=2)
boton_serie_de_Taylor.pack(pady=10, padx=100)

boton_Ceros_de_Funciones = tk.Button(root, text="Ceros de Funciones", command=abrir_ceros, width=25, height=2)
boton_Ceros_de_Funciones.pack(pady=10, padx=100)

boton_Sistemas_de_ecuaciones_lineales = tk.Button(root, text="Sistemas de Ecuaciones Lineales", command=abrir_sistemas_ecuaciones, width=25, height=2)
boton_Sistemas_de_ecuaciones_lineales.pack(pady=10, padx=100)

boton_Interpolación_ajuste = tk.Button(root, text="Interpolación Ajuste", command=abrir_interpolacion, width=25, height=2)
boton_Interpolación_ajuste.pack(pady=10, padx=100)

boton_Ecuaciones_diferenciales = tk.Button(root, text="Ecuaciones Diferenciales", command=abrir_ecuaciones_diferenciales, width=25, height=2)
boton_Ecuaciones_diferenciales.pack(pady=10, padx=100)

root.mainloop()
