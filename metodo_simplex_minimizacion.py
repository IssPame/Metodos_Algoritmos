import numpy as np


Fun_obj_x1 = 0.12 #float(input("Ingrese el valor de x1 en la función objetivo: "))
Fun_obj_x2 = 0.15 #float(input("Ingrese el valor de x2 en la función objetivo: "))

Ecu1_x1 = 60 #float(input("\nIngrese el valor de x1 en la primera Restricción: "))
Ecu1_x2 = 60 #float(input("Ingrese el valor de x2 en la primera Restricción: "))
Valor_Ecu1 = 300 #float(input("Ingrese el valor de la primera Restricción: "))

Ecu2_x1 = 12 #float(input("\nIngrese el valor de x1 en la segunda restricción: "))
Ecu2_x2 =  6 #float(input("Ingrese el valor de x2 en la segunda restricción: "))
Valor_Ecu2 = 36 #float(input("Ingrese el valor de la segunda Restricción: "))

Ecu3_x1 = 10 #float(input("\nIngrese el valor de x1 en la tercera restricción: "))
Ecu3_x2 = 30 #float(input("Ingrese el valor de x2 en la tercera restricción: "))
Valor_Ecu3 = 90 #float(input("Ingrese el valor de la tercera Restricción: "))

matriz = np.array([[-1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                   [0, Ecu1_x1, Ecu1_x2, -1, 1, 0, 0, 0, 0, Valor_Ecu1],
                   [0, Ecu2_x1, Ecu2_x2, 0, 0, -1, 1, 0, 0, Valor_Ecu2],
                   [0, Ecu3_x1, Ecu3_x2, 0, 0, 0, 0, -1, 1, Valor_Ecu3]], dtype=float)


print("\nMatriz inicial: \n", matriz)

if matriz[0][1] >= 0 and matriz[0][2] >= 0:
    for j in range(matriz.shape[1]):
        suma = 0
        for i in range(matriz.shape[0]):
            if i != 0:
                suma += matriz[i][j]
        matriz[0][j] = matriz[0][j] - suma

    print("\nEliminación gaussiana: \n", matriz)


def pivotear(A):
    # calcular la columna menor
    valor_menor = 0
    for j in range(A.shape[1]):
        if j != 0:
            if j == (len(range(A.shape[1])) - 1):
                break
            if A[0][j] < valor_menor:
                valor_menor = A[0][j]
                columna_pivote = j

    print(valor_menor)

    while valor_menor < 0:
        print("\nValor menor: ", valor_menor)

        print("\nColumna pivote: ", columna_pivote)

        # Calcular la fila pivote
        minimo = 0
        for i in range(A.shape[0]):
            if i != 0:
                if A[i][columna_pivote] != 0:
                    division = A[i][9] / A[i][columna_pivote]
                    if i == 1 and division > 0:
                        minimo = division
                        fila_pivote = i
                    else:
                        if (division < minimo) and (division > 0):
                            minimo = division
                            fila_pivote = i

        print("\nFila pivote: ", fila_pivote)

        valor_pivote = A[fila_pivote][columna_pivote]

        # dividir la fila pivote
        for j in range(A.shape[1]):
            A[fila_pivote][j] = A[fila_pivote][j] / valor_pivote

        for i in range(A.shape[0]):
            if i != fila_pivote:
                valor_columna_pivote = A[i][columna_pivote]
                print(valor_columna_pivote)
                for j in range(A.shape[1]):
                    A[i][j] = A[i][j] - (A[fila_pivote][j] * valor_columna_pivote)

        valor_menor = 0
        for j in range(A.shape[1]):
            if j != 0:
                if j == (len(range(A.shape[1])) - 1):
                    break
                if A[0][j] < valor_menor:
                    valor_menor = A[0][j]
                    columna_pivote = j

        print("\n", A)


pivotear(matriz)

