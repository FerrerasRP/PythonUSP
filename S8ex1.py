def imprime_matriz(matriz):
    linha = 0
    coluna = 0 
    while linha <= len(matriz)-1:

        while coluna <= len(matriz[0])-1:

            print(matriz[linha][coluna], end = " ")

            coluna = coluna + 1

        print("")
        coluna = 0 
        linha = linha + 1
