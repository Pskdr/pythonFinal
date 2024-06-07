import tkinter as tk
from tkinter import Toplevel, messagebox
import numpy as np

def abrir_sistemas_ecuaciones():
    def resolver_sistema():
        try:
            n = int(entry_n.get())
            A = []
            b = []
            for i in range(n):
                fila = list(map(float, entries_A[i].get().split()))
                if len(fila) != n:
                    raise ValueError("Cada fila de la matriz A debe tener n elementos.")
                A.append(fila)
                b.append(float(entries_b[i].get()))

            A = np.array(A)
            b = np.array(b)
            metodo = metodo_var.get()

            if metodo == "Eliminación Gaussiana":
                sol = np.linalg.solve(A, b)
            elif metodo == "Pivoteo":
                sol = pivoteo(A, b)
            elif metodo == "Gauss-Seidel":
                sol = gauss_seidel(A, b)
            else:
                raise ValueError("Método no reconocido.")

            label_resultado.config(text=f"Solución: {sol}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def pivoteo(A, b):
        n = len(b)
        for i in range(n):
            max_fila = np.argmax(np.abs(A[i:n, i])) + i
            if A[max_fila, i] == 0:
                raise ValueError("El sistema no tiene solución única.")
            A[[i, max_fila]] = A[[max_fila, i]]
            b[[i, max_fila]] = b[[max_fila, i]]
            for j in range(i+1, n):
                factor = A[j, i] / A[i, i]
                A[j, i:] -= factor * A[i, i:]
                b[j] -= factor * b[i]
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        return x

    def gauss_seidel(A, b, tol=1e-10, max_iter=1000):
        n = len(b)
        x = np.zeros(n)
        for k in range(max_iter):
            x_new = np.copy(x)
            for i in range(n):
                s1 = np.dot(A[i, :i], x_new[:i])
                s2 = np.dot(A[i, i+1:], x[i+1:])
                x_new[i] = (b[i] - s1 - s2) / A[i, i]
            if np.linalg.norm(x_new - x, ord=np.inf) < tol:
                return x_new
            x = x_new
        raise ValueError("El método Gauss-Seidel no convergió")

    nueva_ventana = Toplevel()
    nueva_ventana.title("Sistemas de Ecuaciones Lineales")

    global entry_n, entries_A, entries_b, label_resultado, metodo_var

    label_n = tk.Label(nueva_ventana, text="Número de ecuaciones:")
    label_n.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    entry_n = tk.Entry(nueva_ventana, width=10)
    entry_n.grid(row=0, column=1, padx=5, pady=5, sticky='w')

    label_A = tk.Label(nueva_ventana, text="Matriz A (una fila por línea):")
    label_A.grid(row=1, column=0, padx=5, pady=5, sticky='w')

    entries_A = []
    for i in range(10):
        entry = tk.Entry(nueva_ventana, width=50)
        entry.grid(row=2 + i, column=0, columnspan=2, padx=5, pady=2, sticky='w')
        entries_A.append(entry)

    label_b = tk.Label(nueva_ventana, text="Vector b (una entrada por línea):")
    label_b.grid(row=1, column=2, padx=5, pady=5, sticky='w')

    entries_b = []
    for i in range(10):
        entry = tk.Entry(nueva_ventana, width=20)
        entry.grid(row=2 + i, column=2, padx=5, pady=2, sticky='w')
        entries_b.append(entry)

    label_metodo = tk.Label(nueva_ventana, text="Método:")
    label_metodo.grid(row=12, column=0, padx=5, pady=5, sticky='w')
    metodo_var = tk.StringVar(value="Eliminación Gaussiana")
    metodos = ["Eliminación Gaussiana", "Pivoteo", "Gauss-Seidel"]
    for i, metodo in enumerate(metodos):
        rb = tk.Radiobutton(nueva_ventana, text=metodo, variable=metodo_var, value=metodo)
        rb.grid(row=12 + i, column=1, padx=5, pady=2, sticky='w')

    boton_resolver = tk.Button(nueva_ventana, text="Resolver Sistema", command=resolver_sistema)
    boton_resolver.grid(row=15, column=0, columnspan=3, pady=10)

    label_resultado = tk.Label(nueva_ventana, text="")
    label_resultado.grid(row=16, column=0, columnspan=3, pady=10)

