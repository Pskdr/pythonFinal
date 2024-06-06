import tkinter as tk
from tkinter import Toplevel
from sympy import symbols, diff, lambdify, sympify
import matplotlib.pyplot as plt
import numpy as np

def calcular_serie_de_taylor():
    try:
        x = symbols('x')
        funcion = sympify(entry_funcion.get())
        grado = int(entry_grado.get())
        x0 = float(entry_x0.get())
        
        # Calcular los términos de la serie de Taylor
        taylor_series = funcion
        for i in range(1, grado + 1):
            derivada = diff(funcion, x, i)
            termino = (derivada.subs(x, x0) / np.math.factorial(i)) * (x - x0)**i
            taylor_series += termino
        
        taylor_series = taylor_series.simplify()
        label_resultado.config(text=f"Polinomio de Taylor: {taylor_series}")

        # Graficar la función y el polinomio de Taylor
        funcion_lambdified = lambdify(x, funcion, modules=['numpy'])
        taylor_lambdified = lambdify(x, taylor_series, modules=['numpy'])

        x_vals = np.linspace(x0 - 5, x0 + 5, 400)
        y_vals_funcion = funcion_lambdified(x_vals)
        y_vals_taylor = taylor_lambdified(x_vals)

        plt.figure()
        plt.plot(x_vals, y_vals_funcion, label='Función Original')
        plt.plot(x_vals, y_vals_taylor, label=f'Polinomio de Taylor (grado {grado})')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Serie de Taylor')
        plt.grid(True)
        plt.show()

    except Exception as e:
        label_resultado.config(text=f"Error: {e}")

def abrir_metodo_de_taylor():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Método de Taylor")

    global entry_funcion, entry_grado, entry_x0, label_resultado

    label_funcion = tk.Label(nueva_ventana, text="Función en x (usar 'x' como variable):")
    label_funcion.pack(pady=5)
    entry_funcion = tk.Entry(nueva_ventana, width=50)
    entry_funcion.pack(pady=5)

    label_x0 = tk.Label(nueva_ventana, text="Valor de x0:")
    label_x0.pack(pady=5)
    entry_x0 = tk.Entry(nueva_ventana, width=50)
    entry_x0.pack(pady=5)

    label_grado = tk.Label(nueva_ventana, text="Grado del polinomio:")
    label_grado.pack(pady=5)
    entry_grado = tk.Entry(nueva_ventana, width=50)
    entry_grado.pack(pady=5)

    boton_calcular = tk.Button(nueva_ventana, text="Calcular Serie de Taylor", command=calcular_serie_de_taylor)
    boton_calcular.pack(pady=10)

    label_resultado = tk.Label(nueva_ventana, text="")
    label_resultado.pack(pady=10)

