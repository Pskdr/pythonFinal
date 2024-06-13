import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Funciones de resolución de ecuaciones diferenciales
def euler(f, a, b, h, y0, dy0=None):
    n = int((b - a) / h)
    y = [y0]
    dy = [dy0] if dy0 is not None else None
    t = np.linspace(a, b, n + 1)
    for i in range(n):
        y.append(y[i] + h * (dy[i] if dy else f(t[i], y[i])))
        if dy:
            dy.append(dy[i] + h * f(t[i], y[i], dy[i]))
    return t, y

def runge_kutta(f, a, b, y0, dy0, h):
    n = int((b - a) / h)
    y = [y0]
    dy = [dy0]
    t = np.linspace(a, b, n + 1)
    for i in range(n):
        k1 = h * dy[i]
        l1 = h * f(t[i], y[i], dy[i])
        k2 = h * (dy[i] + l1 / 2)
        l2 = h * f(t[i] + h / 2, y[i] + k1 / 2, dy[i] + l1 / 2)
        k3 = h * (dy[i] + l2 / 2)
        l3 = h * f(t[i] + h / 2, y[i] + k2 / 2, dy[i] + l2 / 2)
        k4 = h * (dy[i] + l3)
        l4 = h * f(t[i] + h, y[i] + k3, dy[i] + l3)
        y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        dy.append(dy[i] + (l1 + 2 * l2 + 2 * l3 + l4) / 6)
    return t, y

def abrir_ecuaciones_diferenciales():
    ventana_ed = tk.Toplevel()
    ventana_ed.title("Ecuaciones Diferenciales")

    # Interfaz gráfica
    tk.Label(ventana_ed, text="Ecuación diferencial (función de t, y, y'):").grid(row=0, column=0)
    entry_eq = tk.Entry(ventana_ed, width=50)
    entry_eq.grid(row=0, column=1)

    tk.Label(ventana_ed, text="Intervalo de t (a, b):").grid(row=1, column=0)
    entry_intervalo = tk.Entry(ventana_ed, width=20)
    entry_intervalo.grid(row=1, column=1)

    tk.Label(ventana_ed, text="Condición inicial y(a):").grid(row=2, column=0)
    entry_y0 = tk.Entry(ventana_ed, width=20)
    entry_y0.grid(row=2, column=1)

    entry_dy0 = tk.Entry(ventana_ed, width=20)
    entry_dy0.grid(row=3, column=1)
    label_dy0 = tk.Label(ventana_ed, text="Condición inicial y'(a):")
    label_dy0.grid(row=3, column=0)
    label_dy0.grid_remove()  # Ocultar el campo y'(a) inicialmente

    tk.Label(ventana_ed, text="Paso h:").grid(row=4, column=0)
    entry_h = tk.Entry(ventana_ed, width=20)
    entry_h.grid(row=4, column=1)

    tk.Label(ventana_ed, text="Tipo de Ecuación:").grid(row=5, column=0)
    tipo_var = tk.StringVar(value="Primer Orden")
    opciones = ["Primer Orden", "Segundo Orden"]
    menu_tipo = tk.OptionMenu(ventana_ed, tipo_var, *opciones)
    menu_tipo.grid(row=5, column=1)

    tk.Label(ventana_ed, text="Método de Resolución:").grid(row=6, column=0)
    metodo_var = tk.StringVar(value="Euler")
    opciones = ["Euler", "Runge-Kutta"]
    menu_metodo = tk.OptionMenu(ventana_ed, metodo_var, *opciones)
    menu_metodo.grid(row=6, column=1)

    label_resultado = tk.Label(ventana_ed, text="", justify=tk.LEFT)
    label_resultado.grid(row=8, columnspan=2, pady=10)

    def resolver_ecuacion():
        try:
            # Obtener la función lambda desde el input del usuario
            eq_str = entry_eq.get().strip()

            # Definir la función lambda adecuadamente
            if tipo_var.get() == "Primer Orden":
                f = lambda t, y, dy=None: eval(eq_str, {'np': np, 't': t, 'y': y, 'dy': dy})
            elif tipo_var.get() == "Segundo Orden":
                f = lambda t, y, dy: eval(eq_str, {'np': np, 't': t, 'y': y, 'dy': dy})

            # Obtener los valores de los otros parámetros
            a, b = map(float, entry_intervalo.get().split(','))
            y0 = float(entry_y0.get())
            dy0 = float(
                entry_dy0.get()) if tipo_var.get() == "Segundo Orden" else 0.0  # Cambiado a 0.0 en lugar de None
            h = float(entry_h.get())
            metodo = metodo_var.get()

            # Resolver la ecuación diferencial usando el método seleccionado
            if metodo == "Euler":
                t, y = euler(f, a, b, h, y0, dy0)
            elif metodo == "Runge-Kutta":
                t, y = runge_kutta(f, a, b, y0, dy0, h)

            # Actualizar el label con un mensaje de éxito
            label_resultado.config(text=f"Solución calculada con el método {metodo}.")

            # Graficar el resultado
            plot_result(t, y, metodo)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos para los parámetros.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def toggle_dy0(*args):
        if tipo_var.get() == "Segundo Orden":
            label_dy0.grid()
        else:
            label_dy0.grid_remove()
            entry_dy0.delete(0, tk.END)

    tipo_var.trace("w", toggle_dy0)

    tk.Button(ventana_ed, text="Calcular", command=resolver_ecuacion).grid(row=7, columnspan=2, pady=10)

def plot_result(t, y, metodo):
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label=f'Solución {metodo}', color='blue')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.title(f'Solución de la Ecuación Diferencial usando {metodo}')
    plt.show()