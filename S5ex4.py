def maximo(a, b, c):
    if (a > b) and (a > c):
        return a
    else:
        if (b > a) and (b > c):
            return b
        else:
            return c

def teste():
    assert maximo(30,14,10) == 30
    assert maximo(0,-1,1) == 1
