def soma_elementos(lista):
    i = 0
    soma = 0
    
    while i <= len(lista)-1:
        soma = soma + lista[i]
        i = i + 1
        
    return soma
