n = int(input("Digite um número inteiro:"))
igual = False

while not(igual) and n > 0:
    digito = n % 10
    dezena = (n // 10) % 10

    if digito == dezena:
        igual = True

    n = n // 10

if igual:
    print("sim")
else:
    print("não")
    
