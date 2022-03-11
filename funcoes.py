import numpy as np


def calculaDeterminantes(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4, casas_decimais=3):
    matrizPrimaria = [[a1,a2,a3], [b1,b2,b3], [c1,c2,c3]]
    resultados = [a4,b4,c4]

    matriz = np.array(matrizPrimaria)
    solucao = np.linalg.solve(matriz,resultados)
    determinantes = [round(solucao[0],casas_decimais), round(solucao[1],casas_decimais), round(solucao[2],casas_decimais)]

    return determinantes
