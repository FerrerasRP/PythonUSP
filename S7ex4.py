def remove_repetidos(lista):
    i = 0
    while i < len(lista) - 1:
        contagem = lista.count(lista[i])

        while contagem > 1:
            del lista[lista.index(lista[i])]
            contagem = lista.count(lista[i])

        i = i + 1

    lista.sort()
    
    return lista
      
