# encoding: utf-8

''' ///////////////// descrição da atualiçãoc ///////////////

Trocar jogador

////////////////////////////////////////////////////////////////

'''

def PosicaoJogador(posicao):
	posicaoLC = {
				1:(2,0),
				2:(2,1),
				3:(2,2),
				4:(1,0),
				5:(1,1),
				6:(1,2),
				7:(0,0),
				8:(0,1),
				9:(0,2)
				}
	
	
	if posicao in posicaoLC:	
		# posicaoLC[posicao] == linha , coluna (0,1)	
		posicaoTabela = posicaoLC[posicao]
		posicaoTabelaL = posicaoTabela[0]
		posicaoTabelaC = posicaoTabela[1]
		#tabela[posicaoTabelaL][posicaoTabelaC] = jogador
		return posicaoTabelaL, posicaoTabelaC

		
		
	else:
		print('Posição nao é valicada, digite um número de 1 a 9')
		return -1
tabela = [
			['0','0','0'],
			['0','0','0'],
			['0','0','0']
		 ]

def PreencherTabela(posicao):
	posicaoL = posicao[0]
	posicaoC = posicao[1]
	#print(tabela[posicaoL][posicaoC])
	if jogador != tabela[posicaoL][posicaoC]:
		tabela[posicaoL][posicaoC] = jogador
		for x in range(len(tabela)):
			print(tabela[x])
			#AlteraJogador(jogador)
		print(tabela[posicaoL][posicaoC])
		'''
		if jogador == jogadorA:
			jogador = jogadorB
		else:
			jogador = jogadorA'''
	else:
		print('Campo ja preenchido \n ' 
				'jogue novamente!')
	
def TrocarJogador(jogador):
	if jogador == jogadorA:
		jogador = jogadorB
		return jogador
	else:
		jogador = jogadorA
		return jogador



#variaveis
jogadorA = '1'
jogadorB = '2'
jogador = jogadorA



# while true == roda o jogoa

while True:
	user = input('posição :')
	#user = input('posição :')
	#posicao = input('digite posição')
	if user == 0:
		break
	else:
		posicao = PosicaoJogador(user)
		PreencherTabela(posicao)
		jogador = TrocarJogador(jogador)
		

