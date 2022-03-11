import numpy as np



matrizPrimaria = []
resultados = []
for i in range(4):
    for j in range(4):
        print("Digite o valor da matriz na posição [{},{}]: ".format(i,j), end="")
     
        if(j == 3):
            resultados.append(float(input()))
        else:
            matrizPrimaria.append(float(input()))

linhaA = [ matrizPrimaria[0], matrizPrimaria[1], matrizPrimaria[2]]
linhaB = [ matrizPrimaria[3], matrizPrimaria[4], matrizPrimaria[5]]
linhaC = [ matrizPrimaria[6], matrizPrimaria[7], matrizPrimaria[8]]
resultados.pop()


print(linhaA, linhaB, linhaC)

matriz = np.array([linhaA, linhaB, linhaC])
solucao = np.linalg.solve(matriz,resultados)

determinanteA = solucao[0]
determinanteB = solucao[1]
determinanteC = solucao[2]

print("Determinante A: {}".format(determinanteA) + "\n" + "Determinante B: {}".format(determinanteB) + "\n" + "Determinante C: {}".format(determinanteC))


