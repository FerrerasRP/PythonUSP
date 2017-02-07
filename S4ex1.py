n = int(input("Digite o valor de n: "))
soma = n
i = 1

if n == 0:
    soma = 1
else:
    while i != n:
        soma = soma * (n-i)
        i = i + 1

print(soma)

