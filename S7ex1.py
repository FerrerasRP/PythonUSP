n = int(input("Digite um número: "))
sequencia = []

while n != 0:
    sequencia.append(n)
    n = int(input("Digite um número: "))

i = len(sequencia)-1

while i >= 0:
    print(sequencia[i])
    i = i - 1
    

