import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Funciones de resolución de ecuaciones diferenciales

def euler(f, a, b, h, co):
    n = int((b - a) / h)
    yeu = [co]  # y_euler
    t = np.linspace(a, b, n + 1)
    for i in range(n):
        yeu.append(yeu[i] + h * f(t[i], yeu[i]))
    return t, yeu

def runge_kutta(dy, x0, x_final, y0, h):
    x_values = np.arange(x0, x_final, h)
    y_values = [y0]
    y = y0

    for x in x_values[:-1]:
        k1 = h * dy(x, y)
        k2 = h * dy(x + h / 2, y + k1 / 2)
        k3 = h * dy(x + h / 2, y + k2 / 2)
        k4 = h * dy(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y_values.append(y)
    return x_values, y_values

# Función para abrir la ventana de ecuaciones diferenciales

def abrir_ecuaciones_diferenciales():
    ventana_ed = tk.Toplevel()
    ventana_ed.title("Ecuaciones Diferenciales")

    # Interfaz gráfica
    tk.Label(ventana_ed, text="Ecuación diferencial (función de t y y):").grid(row=0, column=0)
    entry_eq = tk.Entry(ventana_ed, width=50)
    entry_eq.grid(row=0, column=1)

    tk.Label(ventana_ed, text="Intervalo de t (a, b):").grid(row=1, column=0)
    entry_intervalo = tk.Entry(ventana_ed, width=20)
    entry_intervalo.grid(row=1, column=1)

    tk.Label(ventana_ed, text="Condición inicial (y(a)):").grid(row=2, column=0)
    entry_y0 = tk.Entry(ventana_ed, width=20)
    entry_y0.grid(row=2, column=1)

    tk.Label(ventana_ed, text="Paso h:").grid(row=3, column=0)
    entry_h = tk.Entry(ventana_ed, width=20)
    entry_h.grid(row=3, column=1)

    tk.Label(ventana_ed, text="Método de Resolución:").grid(row=4, column=0)
    metodo_var = tk.StringVar(value="Euler")
    opciones = ["Euler", "Runge-Kutta"]
    menu_metodo = tk.OptionMenu(ventana_ed, metodo_var, *opciones)
    menu_metodo.grid(row=4, column=1)

    label_resultado = tk.Label(ventana_ed, text="", justify=tk.LEFT)
    label_resultado.grid(row=6, columnspan=2, pady=10)

    def resolver_ecuacion():
        try:
            f = eval(f"lambda t, y: {entry_eq.get()}")
            a, b = map(float, entry_intervalo.get().split(','))
            y0 = float(entry_y0.get())
            h = float(entry_h.get())
            metodo = metodo_var.get()

            if metodo == "Euler":
                t, y = euler(f, a, b, h, y0)
            elif metodo == "Runge-Kutta":
                t, y = runge_kutta(f, a, b, y0, h)

            label_resultado.config(text=f"Solución calculada con el método {metodo}.")
            plot_result(t, y, metodo)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana_ed, text="Calcular", command=resolver_ecuacion).grid(row=5, columnspan=2, pady=10)

def plot_result(t, y, metodo):
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label=f'Solución {metodo}', color='blue')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.title(f'Solución de la Ecuación Diferencial usando {metodo}')
    plt.show()