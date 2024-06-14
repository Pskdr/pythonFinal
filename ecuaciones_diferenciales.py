import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import matplotlib.pyplot as plt

def euler(f, a, b, h, y0, dy0=None):
    n = int((b - a) / h)
    y = [y0]
    dy = [dy0] if dy0 is not None else None
    t = np.linspace(a, b, n + 1)
    for i in range(n):
        if dy:
            y.append(y[i] + h * dy[i])
            dy.append(dy[i] + h * f(t[i], y[i], dy[i]))
        else:
            y.append(y[i] + h * f(t[i], y[i]))
    return t, y

def runge_kutta(f, a, b, y0, dy0, h):
    n = int((b - a) / h)
    y = [y0]
    dy = [dy0] if dy0 is not None else None
    t = np.linspace(a, b, n + 1)
    for i in range(n):
        if dy:
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
        else:
            k1 = h * f(t[i], y[i])
            k2 = h * f(t[i] + h / 2, y[i] + k1 / 2)
            k3 = h * f(t[i] + h / 2, y[i] + k2 / 2)
            k4 = h * f(t[i] + h, y[i] + k3)
            y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return t, y

def abrir_ecuaciones_diferenciales():
    ventana_ed = tk.Toplevel()
    ventana_ed.title("Ecuaciones Diferenciales")

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
    label_dy0.grid_remove()

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

    tree = ttk.Treeview(ventana_ed, columns=("t", "y"), show="headings", height=8)
    tree.heading("t", text="t")
    tree.heading("y", text="y")
    tree.grid(row=9, columnspan=2, pady=10, padx=10)

    label_resultado = tk.Label(ventana_ed, text="", justify=tk.LEFT)
    label_resultado.grid(row=8, columnspan=2, pady=10)

    def resolver_ecuacion():
        try:
            eq_str = entry_eq.get().strip()
            es_segundo_orden = tipo_var.get() == "Segundo Orden"
            if es_segundo_orden:
                f = lambda t, y, dy: eval(eq_str, {'np': np, 't': t, 'y': y, 'dy': dy})
            else:
                f = lambda t, y: eval(eq_str, {'np': np, 't': t, 'y': y})

            a, b = map(float, entry_intervalo.get().split(','))
            y0 = float(entry_y0.get())
            dy0 = float(entry_dy0.get()) if es_segundo_orden else None
            h = float(entry_h.get())
            metodo = metodo_var.get()

            if es_segundo_orden and dy0 is None:
                messagebox.showerror("Error",
                                     "Se requiere la condición inicial y'(a) para ecuaciones de segundo orden.")
                return

            if metodo == "Euler":
                t, y = euler(f, a, b, h, y0, dy0)
            elif metodo == "Runge-Kutta":
                t, y = runge_kutta(f, a, b, y0, dy0, h)

            # Limpiamos la tabla antes de llenarla con los nuevos datos
            for row in tree.get_children():
                tree.delete(row)

            # Insertamos los datos en la tabla
            for i in range(len(t)):
                tree.insert("", tk.END, values=(t[i], y[i]))

            label_resultado.config(text=f"Solución calculada con el método {metodo}.")
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