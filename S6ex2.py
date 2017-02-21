def éhipotenusa(n):
    a = 1
    b = 2

    while a < n and b < n:
        if (a*a)+(b*b) == n:
            return True
        else:
            a = a + 1
            b = b + 1
    return False

def soma_hipotenusas(n):
    soma = 0
    i = 1
    while i <= n:
        if éhipotenusa(i):
            soma = soma + i
        i = i + 1

    return soma
