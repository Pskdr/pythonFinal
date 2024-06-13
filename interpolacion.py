import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def polinomial_simple(x_data, y_data):
    n = len(x_data)
    M_p = np.zeros([n, n])
    for i in range(n):
        M_p[i, 0] = 1
        for j in range(1, n):
            M_p[i, j] = M_p[i, j - 1] * x_data[i]
    a_i = np.linalg.solve(M_p, y_data)
    return a_i

def polinomio_lagrange(x_d, y_d):
    x = sp.symbols('x')
    n = len(x_d)
    S = 0
    for i in range(n):
        pr = 1
        for j in range(n):
            if j != i:
                pr *= (x - x_d[j]) / (x_d[i] - x_d[j])
        S += pr * y_d[i]
    return S.expand()

def minimos_cuadrados(xd, yd):
    n = len(xd)
    sx = sum(xd)
    sf = sum(yd)
    sx2 = sum(xd ** 2)
    sfx = sum(xd * yd)
    a0 = (sf * sx2 - sx * sfx) / (n * sx2 - (sx) ** 2)
    a1 = (n * sfx - sf * sx) / (n * sx2 - (sx) ** 2)
    return a0, a1

def graficar_interpolacion(x_data, y_data, metodo, x_val=None):
    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, label='Datos')

    if metodo == "Polinomial Simple":
        coefs = polinomial_simple(x_data, y_data)
        polinomio = np.poly1d(coefs[::-1])
        x_plot = np.linspace(min(x_data), max(x_data), 100)
        y_plot = polinomio(x_plot)
        ax.plot(x_plot, y_plot, label='Polinomio Simple')

    elif metodo == "Lagrange":
        polinomio = polinomio_lagrange(x_data, y_data)
        x = sp.symbols('x')
        x_plot = np.linspace(min(x_data), max(x_data), 100)
        y_plot = [polinomio.subs(x, x_val) for x_val in x_plot]
        ax.plot(x_plot, y_plot, label='Lagrange')

    elif metodo == "Mínimos Cuadrados":
        a0, a1 = minimos_cuadrados(x_data, y_data)
        polinomio = lambda x: a0 + a1 * x
        x_plot = np.linspace(min(x_data), max(x_data), 100)
        y_plot = [polinomio(x) for x in x_plot]
        ax.plot(x_plot, y_plot, label='Mínimos Cuadrados')

    if x_val is not None:
        y_aprox = polinomio(x_val)
        ax.plot(x_val, y_aprox, 'ro', label=f'Punto aproximado ({x_val}, {y_aprox:.2f})')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Interpolación: {metodo}')
    ax.legend()
    plt.show()

def abrir_interpolacion():
    ventana_interpolacion = tk.Toplevel()
    ventana_interpolacion.title("Interpolación y Ajuste de Curvas")

    # Interfaz gráfica
    tk.Label(ventana_interpolacion, text="Datos X (separados por comas):").grid(row=0, column=0)
    entry_x = tk.Entry(ventana_interpolacion, width=50)
    entry_x.grid(row=0, column=1)

    tk.Label(ventana_interpolacion, text="Datos Y (separados por comas):").grid(row=1, column=0)
    entry_y = tk.Entry(ventana_interpolacion, width=50)
    entry_y.grid(row=1, column=1)

    tk.Label(ventana_interpolacion, text="Valor de X para aproximar:").grid(row=2, column=0)
    entry_x_val = tk.Entry(ventana_interpolacion, width=20)
    entry_x_val.grid(row=2, column=1)

    tk.Label(ventana_interpolacion, text="Método de Interpolación:").grid(row=3, column=0)
    metodo_var = tk.StringVar(value="Polinomial Simple")
    opciones = ["Polinomial Simple", "Lagrange", "Mínimos Cuadrados"]
    menu_metodo = tk.OptionMenu(ventana_interpolacion, metodo_var, *opciones)
    menu_metodo.grid(row=3, column=1)

    label_resultado = tk.Label(ventana_interpolacion, text="", justify=tk.LEFT)
    label_resultado.grid(row=5, columnspan=2, pady=10)

    def calcular_interpolacion():
        try:
            x_data = np.array(list(map(float, entry_x.get().split(','))))
            y_data = np.array(list(map(float, entry_y.get().split(','))))
            x_val = float(entry_x_val.get())
            metodo = metodo_var.get()

            if metodo == "Polinomial Simple":
                coefs = polinomial_simple(x_data, y_data)
                polinomio = np.poly1d(coefs[::-1])
                y_aprox = polinomio(x_val)
                resultado = f"Polinomio: {polinomio}\nValor aproximado en x={x_val}: {y_aprox}"

                # Gráfica
                plt.figure()
                plt.scatter(x_data, y_data, label='Datos')
                plt.plot(x_data, polinomio(x_data), label='Ajuste Polinomial')
                plt.scatter(x_val, y_aprox, color='red', label=f'Aproximación en x={x_val}')
                plt.legend()
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('Ajuste Polinomial')
                plt.grid(True)
                plt.show()

            elif metodo == "Lagrange":
                polinomio = polinomio_lagrange(x_data, y_data)
                y_aprox = polinomio.subs(sp.symbols('x'), x_val)
                resultado = f"Polinomio: {polinomio}\nValor aproximado en x={x_val}: {y_aprox}"

                # Gráfica
                plt.figure()
                plt.scatter(x_data, y_data, label='Datos')
                x_graf = np.linspace(min(x_data), max(x_data), 100)
                y_graf = [polinomio.subs(sp.symbols('x'), xx) for xx in x_graf]
                plt.plot(x_graf, y_graf, label='Polinomio de Lagrange')
                plt.scatter(x_val, y_aprox, color='red', label=f'Aproximación en x={x_val}')
                plt.legend()
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('Polinomio de Lagrange')
                plt.grid(True)
                plt.show()

            elif metodo == "Mínimos Cuadrados":
                a0, a1 = minimos_cuadrados(x_data, y_data)
                polinomio = lambda x: a0 + a1 * x
                y_aprox = polinomio(x_val)
                resultado = f"Polinomio: {a0} + {a1}*x\nValor aproximado en x={x_val}: {y_aprox}"

                # Gráfica
                plt.figure()
                plt.scatter(x_data, y_data, label='Datos')
                plt.plot(x_data, polinomio(x_data), label='Ajuste por Mínimos Cuadrados')
                plt.scatter(x_val, y_aprox, color='red', label=f'Aproximación en x={x_val}')
                plt.legend()
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('Ajuste por Mínimos Cuadrados')
                plt.grid(True)
                plt.show()

            label_resultado.config(text=resultado)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana_interpolacion, text="Calcular", command=calcular_interpolacion).grid(row=4, columnspan=2, pady=10)