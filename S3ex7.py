import math

x1 = int(input("Digite ponto 1 coordenada x:"))
y1 = int(input("Digite ponto 1 coordenada y:"))
x2 = int(input("Digite ponto 2 coordenada x:"))
y2 = int(input("Digite ponto 2 coordenada y:"))

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

if distancia >= 10:
    print("longe")
else:
    print("perto")
    
