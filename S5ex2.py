def maximo(a, b):
    if (a > b):
        return a
    else:
        return b

def teste():
    assert maximo(3,4) == 4
    assert maximo(0,-1) == 0
    
