def éprimo(x):
    fator = 2
    if x == 2:
        return True
    
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True
        
def n_primos(n):
    contaprimo = 0;
    while n >= 2:
        if éprimo(n):
            contaprimo = contaprimo + 1
        n = n - 1

    return contaprimo
