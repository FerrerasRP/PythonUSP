l = int(input("digite a largura:"))
a = int(input("digite a altura:"))

il = 1
ia = 1
while ia <= a:
    while il <= l:
        print("#",end="")
        il = il + 1
    print("")
    ia = ia + 1
    il = 1
