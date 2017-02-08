def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        if n % (m+1) == 0:
            return m
        else:
            i = 1
            while i <= m:
                if (n - i) % (m+1) == 0:
                    return i
                i = i + 1
            
def usuario_escolhe_jogada(n, m):
    x = int(input("Quantas pecas voce vai tirar? "))

    while (x>m) or (x<=0) or (x>n):
        x = int(input("Quantas pecas voce vai tirar? "))
        
    if x >= 1 and x <= m:
        return x

def partida():
    n = int(input("Quantas pecas? "))
    m = int(input("Limite de pecas por jogada? "))

    #global limitepecas
    #limitepecas = m

    pecasnamesa = n
    
    if ((m+1)%n) == 0 or (n%(m+1)) == 0:
        print("Voce comeca!")
        QuemJoga = "usuario"
    else:
        print("Computador comeca!")
        QuemJoga = "computador"
        
    while pecasnamesa != 0:
        if QuemJoga == "computador":
            x = computador_escolhe_jogada(pecasnamesa, m)
            print("O computador tirou "+str(x)+" peca(s)")
            pecasnamesa = pecasnamesa - x
            QuemJoga = "usuario"
        else:
            x = usuario_escolhe_jogada(pecasnamesa, m)
            print("Voce tirou "+str(x)+" peca(s)")
            pecasnamesa = pecasnamesa - x
            QuemJoga = "computador"
            
        print("Resta(m) "+str(pecasnamesa)+" peca(s) na mesa")

    if QuemJoga == "computador":
        QuemVence = "usuario"
    else:
        QuemVence = "computador"

    print("Fim do Jogo! O "+QuemVence+" ganhou")
    return QuemVence
        

def campeonato():
    jogo = 1
    placarUsuario = 0
    placarComputador = 0

    while (jogo <= 3):
        print("**** Rodada "+str(jogo)+" ****")

        vencedor = partida()

        if vencedor == "usuario":
            placarUsuario = placarUsuario + 1
        else:
            placarComputador = placarComputador + 1

        jogo = jogo + 1

    print("**** Fim do campeonato! ****")

    print("Placar: Voce "+str(placarUsuario)+" X "+str(placarComputador)+" Computador")
    return

#defini variavel global limite de peças
limitepecas = 1
print("Bem-vindo ao jogo do NIM Escolha:")

print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

tipojogo = int(input())

if tipojogo == 1:
    print("Voce escolheu uma partida isolada")
    partida()
else:
    print("Voce escolheu um campeonato!")
    campeonato()
          
    
