import tkinter as tk
from tkinter import Toplevel
from sympy import symbols, sympify, lambdify
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect, newton, brentq

def abrir_ceros():
    def calcular_ceros():
        try:
            x = symbols('x')
            funcion = sympify(entry_funcion.get())
            funcion_lambdified = lambdify(x, funcion, modules=['numpy'])
            metodo = metodo_var.get()
            tol = float(entry_exactitud.get())
            sol = None
            
            if metodo == "Bisección":
                a, b = float(entry_a.get()), float(entry_b.get())
                if funcion_lambdified(a) * funcion_lambdified(b) >= 0:
                    raise ValueError("f(a) and f(b) must have different signs")
                sol = bisect(funcion_lambdified, a, b, xtol=tol)
            elif metodo == "Newton":
                x0 = float(entry_x0.get())
                sol = newton(funcion_lambdified, x0, tol=tol)
            elif metodo == "Falsa Posición":
                a, b = float(entry_a.get()), float(entry_b.get())
                sol = brentq(funcion_lambdified, a, b, xtol=tol)
            elif metodo == "Secante":
                x0, x1 = float(entry_x0.get()), float(entry_x1.get())
                sol = newton(funcion_lambdified, x0, x1=x1, tol=tol)
            
            label_resultado.config(text=f"Solución: {sol}")

            x_vals = np.linspace(sol - 5, sol + 5, 400)
            y_vals = funcion_lambdified(x_vals)
            
            plt.figure()
            plt.plot(x_vals, y_vals, label='Función')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(sol, color='red', linestyle='--', label='Raíz encontrada')
            plt.legend()
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Ceros de la Función')
            plt.grid(True)
            plt.show()
        
        except Exception as e:
            label_resultado.config(text=f"Error: {e}")

    nueva_ventana = Toplevel()
    nueva_ventana.title("Ceros de Funciones")

    global entry_funcion, entry_a, entry_b, entry_x0, entry_x1, entry_exactitud, label_resultado, metodo_var

    label_funcion = tk.Label(nueva_ventana, text="Función en x (usar 'x' como variable):")
    label_funcion.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    entry_funcion = tk.Entry(nueva_ventana, width=50)
    entry_funcion.grid(row=0, column=1, padx=5, pady=5)

    label_exactitud = tk.Label(nueva_ventana, text="Exactitud (tolerancia):")
    label_exactitud.grid(row=1, column=0, padx=5, pady=5, sticky='w')
    entry_exactitud = tk.Entry(nueva_ventana, width=50)
    entry_exactitud.grid(row=1, column=1, padx=5, pady=5)

    label_metodo = tk.Label(nueva_ventana, text="Método:")
    label_metodo.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    metodo_var = tk.StringVar(value="Bisección")
    metodos = ["Bisección", "Newton", "Falsa Posición", "Secante"]
    for i, metodo in enumerate(metodos):
        rb = tk.Radiobutton(nueva_ventana, text=metodo, variable=metodo_var, value=metodo)
        rb.grid(row=2 + i, column=1, padx=5, pady=2, sticky='w')

    label_intervalo = tk.Label(nueva_ventana, text="Intervalo [a, b] (para Bisección y Falsa Posición):")
    label_intervalo.grid(row=6, column=0, padx=5, pady=5, sticky='w')
    entry_a = tk.Entry(nueva_ventana, width=25)
    entry_a.grid(row=6, column=1, padx=5, pady=5, sticky='w')
    entry_b = tk.Entry(nueva_ventana, width=25)
    entry_b.grid(row=6, column=2, padx=5, pady=5, sticky='w')

    label_punto_inicial = tk.Label(nueva_ventana, text="Punto inicial x0 (para Newton y Secante):")
    label_punto_inicial.grid(row=7, column=0, padx=5, pady=5, sticky='w')
    entry_x0 = tk.Entry(nueva_ventana, width=25)
    entry_x0.grid(row=7, column=1, padx=5, pady=5, sticky='w')
    label_punto_inicial_x1 = tk.Label(nueva_ventana, text="Segundo punto x1 (para Secante):")
    label_punto_inicial_x1.grid(row=8, column=0, padx=5, pady=5, sticky='w')
    entry_x1 = tk.Entry(nueva_ventana, width=25)
    entry_x1.grid(row=8, column=1, padx=5, pady=5, sticky='w')

    boton_calcular = tk.Button(nueva_ventana, text="Calcular Ceros", command=calcular_ceros)
    boton_calcular.grid(row=9, column=0, columnspan=3, pady=10)

    label_resultado = tk.Label(nueva_ventana, text="")
    label_resultado.grid(row=10, column=0, columnspan=3, pady=10)
