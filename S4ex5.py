n = int(input("Digite um número inteiro:"))
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
if primo:
    print("primo")
else:
    print("não primo")
    
