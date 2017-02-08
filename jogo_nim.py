def computador_escolhe_jogada(n, m):
    if (n==1):
        tirar = 1
    else:
        fator = m + 1
        if (n%fator)==0:
            tirar = n-fator
        else:
            tirar = n-1

        if tirar > limitepecas:
            tirar = limitepecas
    
    print("O computador tirou "+str(tirar)+" peca(s)")
    return tirar

def usuario_escolhe_jogada(n, m):
    global limitepecas
    while m > n-1 or m == 0 or m < limitepecas:
        m = int(input("Oops! Jogada invalida! Tente de novo. "))

    return m

def partida():
    n = int(input("Quantas pecas? "))
    m = int(input("Limite de pecas por jogada? "))
    global limitepecas
    limitepecas = m

    pecasnamesa = n
    
    if ((m+1)%n) == 0:
        print("Voce comeca!")
        QuemJoga = "usuario"
    else:
        print("Computador comeca!")
        QuemJoga = "computador"
        
    while pecasnamesa != 0:
        if QuemJoga == "computador":
            m = 1
            pecasnamesa = pecasnamesa - computador_escolhe_jogada(pecasnamesa, m)
            QuemJoga = "usuario"
        else:
            m = int(input("Quantas pecas voce vai tirar? "))
            pecasnamesa = pecasnamesa - usuario_escolhe_jogada(pecasnamesa, m)
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
          
    
