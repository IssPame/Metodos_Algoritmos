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

matriz_fase1 = np.array([["VB", "z", "x1", "x2", "e1", "a1", "e2", "a2", "e3", "a3", "LD"],
                         ["Z", -1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                         ["a1", 0, Ecu1_x1, Ecu1_x2, -1, 1, 0, 0, 0, 0, Valor_Ecu1],
                         ["a2", 0, Ecu2_x1, Ecu2_x2, 0, 0, -1, 1, 0, 0, Valor_Ecu2],
                         ["a3", 0, Ecu3_x1, Ecu3_x2, 0, 0, 0, 0, -1, 1, Valor_Ecu3]])


print("\nMatriz Primera Fase: \n", matriz_fase1)


def eliminicion_gaussiana(matriz):
    for j in range(matriz.shape[1]):
        if j != 0:
            suma = 0
            for i in range(matriz.shape[0]):
                if i != 0:
                    suma += float(matriz[i][j])
            matriz[1][j] = float(matriz_fase1[1][j]) - suma

    print("\nEliminación gaussiana: \n", matriz)


def pivotear(A):
    # calcular la columna menor
    valor_menor = 0
    for j in range(A.shape[1]):
        if j != 0 and j != 1:
            if j == (len(range(A.shape[1])) - 1):
                break
            if float(A[1][j]) < valor_menor:
                valor_menor = float(A[1][j])
                columna_pivote = j

    print(valor_menor)

    while valor_menor < 0:
        print("\nValor menor: ", valor_menor)

        print("\nColumna pivote: ", columna_pivote)

        # Calcular la fila pivote
        minimo = 0
        limite_columna = len(range(A.shape[1])) - 1
        for i in range(A.shape[0]):
            if i != 0 and i != 1:
                if float(A[i][columna_pivote]) != 0:
                    division = float(A[i][limite_columna]) / float(A[i][columna_pivote])
                    if i == 2 and division > 0:
                        minimo = division
                        fila_pivote = i
                    else:
                        if (division < minimo) and (division > 0):
                            minimo = division
                            fila_pivote = i

        print("\nFila pivote: ", fila_pivote)

        valor_pivote = float(A[fila_pivote][columna_pivote])

        # dividir la fila pivote
        for j in range(A.shape[1]):
            if j != 0:
                A[fila_pivote][j] = float(A[fila_pivote][j]) / valor_pivote

        for i in range(A.shape[0]):
            if i != fila_pivote and i != 0:
                valor_columna_pivote = A[i][columna_pivote]
                print(valor_columna_pivote)
                for j in range(A.shape[1]):
                    if j != 0:
                        A[i][j] = float(A[i][j]) - (float(A[fila_pivote][j]) * valor_columna_pivote)

        valor_menor = 0
        for j in range(A.shape[1]):
            if j != 0 and j != 1:
                if j == (len(range(A.shape[1])) - 1):
                    break
                if float(A[0][j]) < valor_menor:
                    valor_menor = float(A[0][j])
                    columna_pivote = j

        print("\n", A)


if float(matriz_fase1[1][2]) >= 0 and float(matriz_fase1[1][3]) >= 0:
    eliminicion_gaussiana(matriz_fase1)
pivotear(matriz_fase1)

matriz_fase2 = np.array([["VB", "Z", "x1", "x2", "e1", "e2", "e3", "LD"],
                         ["Z", matriz_fase1[1][1], Fun_obj_x1, Fun_obj_x2, 0, 0, 0, 0],
                         [matriz_fase1[0][2], 0, 0, 0, matriz_fase1[1][3], matriz_fase1[1][5], matriz_fase1[1][7], matriz_fase1[1][9]],
                         [matriz_fase1[0][3], 0, 1, 0, matriz_fase1[2][3], matriz_fase1[2][5], matriz_fase1[2][7], matriz_fase1[2][9]],
                         [matriz_fase1[0][4], 0, 0, 1, matriz_fase1[3][3], matriz_fase1[3][5], matriz_fase1[3][7], matriz_fase1[3][9]]])

print("\nMatriz Segunda Fase: \n", matriz_fase2)
if float(matriz_fase2[1][2]) >= 0 and float(matriz_fase2[1][3]) >= 0:
    eliminicion_gaussiana(matriz_fase2)
# pivotear(matriz_fase2)


