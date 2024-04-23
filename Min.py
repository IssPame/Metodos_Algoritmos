import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definicion de los simbolos
x, y = sp.symbols('x, y')

# Funcion Objetivo
F_Obj_x = float(input("Indique el valor de X1 (x) en la función objetivo: "))
F_Obj_y = float(input("Indique el valor de X2 (y) en la función objetivo: "))
Z = F_Obj_x*x + F_Obj_y*y
print("La función objetivo es: Z = ", Z)
print()

# Solicitar el numero de restricciones
Restricciones = int(input("Indique cuántas restricciones serán: "))

# Inicializar listas para almacenar los valores de las restricciones
restricciones = []

# Solicitar los valores de las restricciones
for i in range(Restricciones):
    print()
    Ec_x = float(input(f"Indique el valor de X1 (x) en la restricción {i+1}: "))
    Ec_y = float(input(f"Indique el valor de X2 (y) en la restricción {i+1}: "))
    ValorEc = float(input(f"Indique el valor de la restricción {i+1}: "))
    restricciones.append((Ec_x, Ec_y, ValorEc))
print()

# Imprimir las restricciones ingresadas
for i, (Ec_x, Ec_y, ValorEc) in enumerate(restricciones, start=1):
    print(f"Restricción {i}: {Ec_x}*x1 + {Ec_y}*x2 = {ValorEc}")
print()

# Definir el rango de valores para x y y
Rango_Val_x = np.linspace(0, 50, 100)
Rango_Val_y = np.linspace(0, 50, 100)

# Crear una cuadricula de puntos (x, y)
X, Y = np.meshgrid(Rango_Val_x, Rango_Val_y)

# Evaluar la funcion objetivo y las restricciones en todos los puntos de la cuadricula
Z_vals = F_Obj_x*X + F_Obj_y*Y
restricciones_vals = np.array([Ec_x*X + Ec_y*Y - ValorEc for Ec_x, Ec_y, ValorEc in restricciones])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Trazar la funcion objetivo
ax.contour(X, Y, Z_vals, levels=np.linspace(Z_vals.min(), Z_vals.max(), 10), alpha=0.5)

# Trazar las restricciones
for r in restricciones_vals:
    ax.contour(X, Y, r, levels=[0], colors='r')

# Configurar los ejes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Función objetivo y restricciones')

# Mostrar la grafica
plt.show()