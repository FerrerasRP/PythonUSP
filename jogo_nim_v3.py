def computador_escolhe_jogada(n, m):
    multiplo = m + 1
    jogada = 1
    while True:
        if (n - jogada) % multiplo == 0:
            print ("Computador retirou: "+str(jogada))
            return jogada
        jogada += 1
		
def usuario_escolhe_jogada(n, m):
    while True:
        valor = int(input("\nInforme o valor da jogada. Entre 1 e {} (Restam {}): ".format(m, n)))
        if valor >= 1 and valor <= m:
            return valor
        print ("Voce deve informar um valor entre 1 e "+format(m))
	
def partida():
	valor_m = 0
	valor_n = 0
	while not valor_m:
		try:
			valor_n = int(input("Quantas Pecas? "))
			valor_m = int(input("Limite de pecas por jogada? "))
		except ValueError:
			print ("Informe um valor valido para M e N")
	
	vez_computador = True
	if valor_n % valor_m == 0:
		vez_computador = False
		print ("Voce Comeca!")
	else:
		print ("O computador comeca")
	while valor_n > 0:
		if vez_computador:
			valor_n -= computador_escolhe_jogada(valor_n, valor_m)
			vez_computador = False # altera para no proximo loop ser o jogador
		else:
			valor_n -= usuario_escolhe_jogada(valor_n, valor_m)
			vez_computador = True
	
	# se a proxima vez for do computador, entao quem ganhou foi o jogador
	if vez_computador:
		print ("\n\nVoce Ganhou!")
	else:
		print ("\n\nO Computador Ganhou!")
			
if __name__ == '__main__':
	partida()
