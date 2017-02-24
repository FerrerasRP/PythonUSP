def soma_matrizes(m1, m2):
    if str(len(m1))+str(len(m1[0])) == str(len(m2))+str(len(m2[0])):
        linha = 0
        coluna = 0
        soma = []
        while linha <= len(m1)-1:
            m_linha = []
            while coluna <= len(m1[0])-1:
                m_linha.append(m1[linha][coluna]+m2[linha][coluna])
                coluna = coluna + 1

            soma.append(m_linha)
            coluna = 0 
            linha = linha + 1

        return soma

    else:
        return False
    
