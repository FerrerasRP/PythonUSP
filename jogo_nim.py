def computador_escolhe_jogada(n, m):

    print("O computador tirou 1 peca")
    return n-1

def usuario_escolhe_jogada(n, m):
    while m > n-1 or m == 0:
        m = int(input("Oops! Jogada invalida! Tente de novo."))

    return (n-m)

def partida():
    n = int(input("Quantas pecas? "))
    m = int(input("Limite de pecas por jogada? "))
    pecasnamesa = n
    
    if ((m+1)%n) == 0:
        print("Voce comeca!")
        QuemJoga = "usuario"
    else:
        print("Computador comeca!")
        QuemJoga = "computador"
        
    while pecasnamesa != 0:
        if QuemJoga == "computador":
            pecasnamesa = computador_escolhe_jogada(pecasnamesa, m)
            QuemJoga = "usuario"
        else:
            m = int(input("Quantas pecas voce vai tirar?"))
            pecasnamesa = usuario_escolhe_jogada(pecasnamesa, m)
            QuemJoga = "computador"

    if QuemJoga == "computador":
        QuemVence = "usuario"
    else:
        QuemVence = "computador"

    print("Fim do Jogo! O "+QuemVence+" ganhou")
        

def campeonato():
    return 0

def main():
    print("Bem-vindo ao jogo do NIM Escolha:")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    tipojogo = int(input())

    if tipojogo == 1:
          print("Voce escolheu uma partida isolada")
    else:
          print("Voce escolheu um campeonato!")
          
    
