def vogal(x):
    if (x=="a") or (x=="e") or (x=="i") or (x=="o") or (x=="u") or (x=="A") or (x=="E") or (x=="I") or (x=="O") or (x=="U"):
        return True
    else:
        return False
        
def teste():
    assert vogal("a") == True
    assert vogal("b") == False
    assert vogal("E") == True
    
