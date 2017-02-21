def maior_elemento(lista):
    i = 0
    if len(lista) == 1:
        return lista[0]
    else:
        while i < len(lista) - 1:
            if lista[i] >= lista[i+1]:
                maior = lista[i]
            else:
                maior = lista[i+1]
            i = i + 1
        return maior
