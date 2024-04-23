import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

x, y = sp.symbols('x, y')

# Función Objetivo
F_Obj_x = float(input("Indique el valor de X1 (x) en la función objetivo: "))
F_Obj_y = float(input("Indique el valor de X2 (y) en la función objetivo: "))
Z = F_Obj_x*x + F_Obj_y*y
print("La función objetivo es: Z = ", Z)
print()

# Solicitar el número de restricciones
num_restricciones = int(input("Indique cuántas restricciones serán: "))

# Inicializar listas para almacenar los valores de las restricciones
restricciones = []

# Solicitar los valores de las restricciones
for i in range(num_restricciones):
    print()
    Ec_x = float(input(f"Indique el valor de X1 (x) en la restricción {i+1}: "))
    Ec_y = float(input(f"Indique el valor de X2 (y) en la restricción {i+1}: "))
    ValorEc = float(input(f"Indique el valor de la restricción {i+1}: "))
    restricciones.append((Ec_x, Ec_y, ValorEc))
print()

# Imprimir las restricciones ingresadas
for i, (Ec_x, Ec_y, ValorEc) in enumerate(restricciones, start=1):
    print(f"Restricción {i}: X1 = {Ec_x}, X2 = {Ec_y}, Valor = {ValorEc}")
print()

# Crear ecuaciones de restricción
ecuaciones = []
for Ec_x, Ec_y, ValorEc in restricciones:
    ecuaciones.append(Ec_x*x + Ec_y*y - ValorEc)

# Imprimir las ecuaciones para depuración
print("Ecuaciones a resolver:")
for ec in ecuaciones:
    print(ec)

# Resolución del sistema
Solucion = sp.solve(ecuaciones, (x, y))

# Verificar si hay soluciones
if not Solucion:
    print("No se encontraron soluciones.")
else:
    # Asumiendo que hay una solución única, seleccionamos la primera
    sol = Solucion[0]

    # Cálculo de las coordenadas de intersección
    Inter_x = sol[x].evalf()
    Inter_y = sol[y].evalf()

    # Cálculo del valor de Z en el punto óptimo
    Z_optimo = F_Obj_x*Inter_x + F_Obj_y*Inter_y

    print("Reemplazamos Z= ", Z, " => Z= ", Z_optimo)

    # Cálculo de las coordenadas de intersección
    Inter_x = sol[x].evalf()
    Inter_y = sol[y].evalf()

    # Cálculo del valor de x e y
    Valor_X = np.arange(0, 50, 0.1)

    # Gráfico
    plt.figure(figsize=(10, 10))

    # Restricciones
    for Ec_x, Ec_y, ValorEc in restricciones:
        Valor_y = (ValorEc - Ec_x * Valor_X) / Ec_y
        plt.plot(Valor_X, Valor_y, label=f'{Ec_x}x + {Ec_y}y = {ValorEc}', color='blue')

    # Pinta región factible
    plt.fill_between(Valor_X, np.min(Valor_y), color='gray', alpha=0.5, label='región factible')

    # Marca punto intersección
    plt.plot(Inter_x, Inter_y, 'ro', label='Intersección')

    # Dibuja la función objetivo sobre el punto óptimo
    plt.plot(Inter_x, Inter_y, 'bo') # Marca punto óptimo
    plt.text(Inter_x, Inter_y, f'Z = {Z_optimo}', ha='right')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Minimización de Z = ' + str(Z))
    plt.legend()
    plt.grid(True)
    plt.show()
