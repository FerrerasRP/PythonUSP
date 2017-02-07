a = int(input("Digite um número inteiro:"))

resto3 = a%3
resto5 = a%5

if resto3 == 0 and resto5 == 0:
    print("FizzBuzz")
else:
    print(a)
