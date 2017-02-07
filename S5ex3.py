def primo(n):
    primo = True
    i = 2

    if n == 1 or n == 2:
        primo = True
    else:
        if (n % 2 == 0):
            primo = False
        else:
            while primo and i <= n/2:
                resto = n % i;
                if resto == 0:
                    primo = False
                i = i + 1
    return primo
   
def maior_primo(n):
    i = n
    while i >= 1:
        if primo(i):
            return i
        i = i - 1
    
def teste():
    assert maior_primo(100) == 97
    assert maior_primo(7) == 7    
