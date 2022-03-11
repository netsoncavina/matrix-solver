import numpy as np

def calculaDeterminantes(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4):
    matrizPrimaria = [[a1,a2,a3], [b1,b2,b3], [c1,c2,c3]]
    resultados = [a4,b4,c4]

    matriz = np.array(matrizPrimaria)
    solucao = np.linalg.solve(matriz,resultados)
    determinantes = [solucao[0], solucao[1], solucao[2]]

    return determinantes

    # print("Determinante A: {}".format(determinanteA) + "\n" + "Determinante B: {}".format(determinanteB) + "\n" + "Determinante C: {}".format(determinanteC))


print(calculaDeterminantes(1,2,3,4,5,6,7,8,9,10,11,12))