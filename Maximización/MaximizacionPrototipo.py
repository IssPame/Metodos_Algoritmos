import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

x, y = sp.symbols('x y')

Fun_Obj_X1 = float(input("Indique el valor de X1 (x) en la funcion objetivo: "))
print()
Fun_Obj_X2 = float(input("Indique el valor de X2 (y) en la funcion objetivo: "))
print()

Z = Fun_Obj_X1 * x + Fun_Obj_X2 * y
print("La funcion objetivo es Z = ", Z)
print()

#Valor de X1,Y1 y X2,Y2 en las ecuaciones
Ecu_X1 = float(input("Indique el valor de X1 (x) en la primera ecuacion: "))
print()
Ecu_Y1 = float(input("Indique el valor de X2 (x) en la primera ecuacion: "))
print()
Val_Ec1 = float(input("Ingrese el valor de la ecuacion: "))

Ecu_X2 = float(input("Indique el valor de X1 (x) en la primera ecuacion: "))
print()
Ecu_Y2 = float(input("Indique el valor de X2 (x) en la primera ecuacion: "))
print()
Val_Ec2 = float(input("Ingrese el valor de la ecuacion: "))


#Restricciones

Rest1 = float(input("Ingrese el valor de la primera restriccion: "))
Rest2 = float(input("Ingrese el valor de la segunda restriccion: "))

#Ecuaciones
Ec1 = sp.Eq(Ecu_X1 * x + Ecu_Y1 * y , Val_Ec1)
Ec2 = sp.Eq(Ecu_X2 * x + Ecu_Y2 * y , Val_Ec2)

#Resolucion del sistema de ecuaciones
Solucion = sp.solve((Ec1, Ec2), (x, y))
Soluc_X = Solucion[x]
Soluc_Y = Solucion[y]

print("Reemplazo en la funcion objetivo: Z = ", Z,"=> Z = ",Fun_Obj_X1 * Soluc_X + Fun_Obj_X2 * Soluc_Y)

# Calculo de las cordenadas de intersecion
Inter_X = Soluc_X.evalf()
Inter_Y = Soluc_Y.evalf()

# Claculo del valor de Z en el punto optimo
Optimo = Fun_Obj_X1 * Inter_X + Fun_Obj_X2 * Inter_Y

#Calculo del valor de X y el valor de Y
Valor_X = np.arange(0, 50, 0.1)
Valor_Y1 = (Val_Ec1 - Ecu_X1 * Valor_X) / Ecu_Y1
Valor_Y2 = (Val_Ec2 - Ecu_X2 * Valor_X) / Ecu_Y2

#Region factible
RegFac = np.minimum(Valor_Y1, Valor_Y2)

# Gráfico
plt.figure(figsize=(10, 10))

# Restricciones
plt.plot(Valor_X, Valor_Y1, label='{}x + {}y = 100'.format(Ecu_X1, Ecu_Y1), color='blue')
plt.plot(Valor_X, Valor_Y2, label='{}x + {}y = 80'.format(Ecu_X2, Ecu_Y2), color='green')

plt.axvline(x=Rest1, color='orange', linestyle='--', label='x1 ≤ {}'.format(Rest1))
plt.axhline(y=Rest2, color='purple', linestyle='--', label='x2 ≤ {}'.format(Rest2))

#Pinta region factible
plt.fill_between(Valor_X, RegFac, color='gray', alpha=0.5, label='Región factible')

#Marca punto de interseccion
plt.plot(Inter_X, Inter_Y, 'ro', label='Interseccion')

#Dibujar la funcion objetivo sobre el punto optimo
plt.plot(Inter_X, Inter_Y, 'bo')  # Marcar el punto óptimo
plt.text(Inter_X, Inter_Y, f'Z = {Optimo}', ha='right')

print("Primera ecuacion: ", Ec1.lhs, "=", Ec1.rhs)
print()
print("Segunda ecuacion: ", Ec2.lhs, "=", Ec2.rhs)
print()
print("Valor de x1:", Soluc_X, "Valor de x2:", Soluc_Y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('No se no se me ocurre que poner de titulo jaja')
plt.legend()
plt.grid(True)
plt.show()