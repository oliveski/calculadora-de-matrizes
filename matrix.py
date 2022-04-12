import random as rng
import sys

###### Funções #######
def escalona_matriz(matriz):
    colunas = len(matriz[0])
    linhas = len(matriz)

    aux = 0
    j = 0
    while aux != 1 and j < colunas:
        n = 0
        for k in range(linhas):
            for i in range(k, linhas):
                if matriz[i][j] != 0:
                    n = i
                    break

            if n > 0 :
                nonzero = matriz[n].copy()
                matriz[n] = matriz[k]
                matriz[k] = nonzero
                n = -1
        if matriz[0][j] == 0:
            j = j + 1
        else:
            break

    if matriz[0][j] != 1 and matriz[0][j] != 0:
        pivot = matriz[0][j]
        for n in range(colunas):    # reduz a primeira linha
            matriz[0][n] = matriz[0][n] / pivot
    
    if colunas >= linhas :
        for k in range(1, linhas):
            for i in range(k, linhas):
                leading = matriz[i][k-1]
                for j in range(colunas):
                    matriz[i][j] = matriz[i][j] - leading * matriz[k-1][j]
            if matriz[k][k] != 0 and matriz[k][k] != 1:
                pivot = matriz[k][k]
                for h in range(k, colunas):
                    matriz[k][h] /= pivot
    else:
        for k in range(1, linhas):
            for i in range(k, linhas):
                leading = matriz[i][k-1]
                for j in range(colunas):
                    matriz[i][j] = matriz[i][j] - leading * matriz[k-1][j]
            if k < colunas:
                if matriz[k][k] != 0 and matriz[k][k] != 1:
                    pivot = matriz[k][k]
                    for h in range(k, colunas, 1):
                        matriz[k][h] /= pivot

    return matriz

def multiplica_matriz():
    print("MULTIPLICAÇÃO DE MATRIZES:")
    print("Duas matrizes são necessárias para a realização da multiplicação.")
    print("Lembre-se que o número de colunas da primeira matriz deve ser o mesmo que o número"
    "de linhas da segunda matriz.")
    print("==== Primeira matriz ====")
    matrizA = recebe_matriz()
    print("==== Segunda matriz ====")
    matrizB = recebe_matriz()

    colunasA = len(matrizA[0])
    linhasA = len(matrizA)
    colunasB = len(matrizB[0])
    linhasB = len(matrizB)
    if (colunasA != linhasB):
        sys.exit("As condições para realização da operação não foram cumpridas!")

    matriz3 = [0] * colunasB
    if (linhasA != 1):
        for i in range(linhasA):
            matriz3[i] = [0] * colunasB
    else:
        matriz3 = [matriz3]

    for k in range(colunasB):
        for i in range(linhasA):
            for j in range(colunasA):
                matriz3[i][k] += matrizA[i][j] * matrizB[j][k]
    return matriz3, matrizA, matrizB


def imprime_matriz(matriz):
    for i in matriz:
        print(i)

def soma_matriz():
    print("SOMA DE MATRIZES:")
    print("Duas matrizes são necessárias para a realização da subtração.")
    print("Lembre-se que elas devem ter o mesmo número de linhas"
    " e o mesmo número de colunas para serem somadas.")
    print("==== Primeira matriz ====")
    matrizA = recebe_matriz()
    print("==== Segunda matriz ====")
    matrizB = recebe_matriz()

    colunasA = len(matrizA[0])
    linhasA = len(matrizA)
    colunasB = len(matrizB[0])
    linhasB = len(matrizB)
    if(linhasA != linhasB or colunasA != colunasB):
        sys.exit("As matrizes não tem as mesmas dimensões!")
    else:
        soma = [0] * linhasA
        for i in range(linhasA):
            soma[i] = [0] * colunasA
        for i in range(linhasA):
            for j in range(colunasA):
                element = matrizA[i][j] + matrizB[i][j]
                soma[i][j] = element
        return soma, matrizA, matrizB

def subtrai_matriz():
    print("SUBTRAÇÃO DE MATRIZES:")
    print("Duas matrizes são necessárias para a realização da subtração.")
    print("Lembre-se que elas devem ter o mesmo número de linhas"
    " e o mesmo número de colunas para serem somadas.")
    print("==== Primeira matriz ====")
    matrizA = recebe_matriz()
    print("==== Segunda matriz ====")
    matrizB = recebe_matriz()

    colunasA = len(matrizA[0])
    linhasA = len(matrizA)
    colunasB = len(matrizB[0])
    linhasB = len(matrizB)
    if(linhasA != linhasB or colunasA != colunasB):
        sys.exit("As matrizes não tem as mesmas dimensões!")
        
    menos = [0] * linhasA
    for i in range(linhasA):
        menos[i] = [0] * colunasA
    for i in range(linhasA):
        for j in range(colunasA):
            element = matrizA[i][j] - matrizB[i][j]
            menos[i][j] = element
    return menos, matrizA, matrizB

def transpor_matriz():
    print("==== Matriz para transpor ====")
    matriz = recebe_matriz()
    linhas = len(matriz)
    colunas = len(matriz[0])
    matriz_t = [0] * colunas
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        matriz_t[j] = nova_linha
    return matriz_t, matriz


def recebe_matriz():
    linhas = int(input("Entre com o número de linhas da matriz: "))
    colunas = int(input("Entre com o número de colunas da matriz: "))

    matriz = [0] * linhas
    for i in range(linhas):
        matriz[i] = [0] * colunas

    tipo = input("Quer entrar com os elementos? (s/n) ")
    if (tipo == 's'):
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                elemento = int(input("({},{}): ".format(i, j)))
                linha.append(elemento)
            matriz[i] = linha
        return matriz
    else:
        LI = int(input("Entre com o limite inferior dos elementos: "))
        LS = int(input("Entre com o limite superior dos elementos: ")) + 1
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                linha.append(rng.randrange(LI, LS))
            matriz[i] = linha
        return matriz

#####################

##### Programa #####

print("Calculadora para a realização de algumas operações envolvendo matrizes com valores inteiros")
print("")
print("Digite '1' Para realizar soma de matrizes.")
print("Digite '2' Para realizar subtração de matrizes.")
print("Digite '3' Para realizar multiplicação de matrizes.")
print("Digite '4' Para realizar a transposição de uma matriz.")
print("Digite '5' Para realizar escalonamento de uma matriz.")
print("")

escolha = int(input("Função: "))
while (escolha != 1) & (escolha != 2) & (escolha != 3) & (escolha != 4) & (escolha != 5):
    print("Operação inexistente! Tente novamente.")
    print("")
    escolha = int(input("Função: "))

if (escolha == 1):
    soma = soma_matriz()
    print("PRIMEIRA MATRIZ:")
    imprime_matriz(soma[1])
    print("")
    print("SEGUNDA MATRIZ:")
    imprime_matriz(soma[2])
    print("")
    print("SOMA DAS MATRIZES:")
    imprime_matriz(soma[0])
elif (escolha == 2):
    subtrai = subtrai_matriz()
    print("PRIMEIRA MATRIZ:")
    imprime_matriz(subtrai[1])
    print("")
    print("SEGUNDA MATRIZ:")
    imprime_matriz(subtrai[2])
    print("")
    print("SUBTRAÇÃO DAS MATRIZES:")
    imprime_matriz(subtrai[0])
elif (escolha == 3):
    multiplica = multiplica_matriz()
    print("PRIMEIRA MATRIZ:")
    imprime_matriz(multiplica[1])
    print("")
    print("SEGUNDA MATRIZ:")
    imprime_matriz(multiplica[2])
    print("")
    print("MULTIPLICAÇÃO DAS MATRIZES:")
    imprime_matriz(multiplica[0])
elif (escolha == 4):
    transposta = transpor_matriz()
    print("MATRIZ ORIGINAL")
    imprime_matriz(transposta[1])
    print("")
    print("MATRIZ TRANSPOSTA")
    imprime_matriz(transposta[0])
elif (escolha == 5):
    print("ESCALONAMENTO:")
    matriz = recebe_matriz()
    print("MATRIZ ORIGINAL")
    imprime_matriz(matriz)
    escalona_matriz(matriz)
    print("MATRIZ ESCALONADA:")
    print("")
    imprime_matriz(matriz)
