# encoding: utf-8

''' ///////////////// descrição da atualiçãoc ///////////////

virifica ganhador

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
		return posicaoTabelaL, posicaoTabelaC

		
		
	else:
		print('Posição nao é valicada, digite um número de 1 a 9')
		return -1


def PreencherTabela(posicao):
	posicaoL = posicao[0]
	posicaoC = posicao[1]	
	if jogador != tabela[posicaoL][posicaoC]:
		tabela[posicaoL][posicaoC] = jogador
		for x in range(len(tabela)):
			print(tabela[x])		
	else:
		print('Campo ja preenchido \n ' 
				'jogue novamente!')
	
def TrocarJogador(jogador):
	print('Ultimo jogador {}'.format(jogador))
	if jogador == jogadorA:
		jogador = jogadorB
		return jogador
	else:
		jogador = jogadorA
		return jogador

def VerificarGanhador(tabela):
	
	vitoriaA = ('111')
	vitoriaB = ('222')
	vitoria1 = tabela[0][2] + tabela[1][1] + tabela[2][0]
	vitoria2 = tabela[0][0] + tabela[0][1] + tabela[0][2]
	vitoria3 = tabela[1][0] + tabela[1][1] + tabela[1][2]
	vitoria4 = tabela[2][0] + tabela[2][1] + tabela[2][2]
	vitoria5 = tabela[0][0] + tabela[1][1] + tabela[2][2]
	vitoria6 = tabela[0][2] + tabela[1][2] + tabela[2][2]
	vitoria7 = tabela[0][1] + tabela[1][1] + tabela[2][1]
	vitoria8 = tabela[0][0] + tabela[1][0] + tabela[2][0]
	
	if vitoria1 == vitoriaA:
		print('jogadorA ganhou')		
		return 'ganhadorA'
	elif vitoria1 == vitoriaB:
		print('jogadorB ganhou')
		return 'ganhadoB'
	elif vitoria2 == vitoriaA:
		print('jogadorA ganhou')		
		return 'ganhadorA'		
	elif vitoria2 == vitoriaB:
		print('jogadorB ganhou')
		return 'ganhadoB'
	elif vitoria3 == vitoriaA:
		print('jogadorA ganhou')		
		return 'ganhadorA'
	elif vitoria3 == vitoriaB:
		print('jogadorB ganhou')
		return 'ganhadoB'
	elif vitoria4 == vitoriaA:
		print('jogadorA ganhou')		
		return 'ganhadorA'
	elif vitoria4 == vitoriaB:
		print('jogadorB ganhou')
		return 'ganhadoB'
	elif vitoria5 == vitoriaA:
		print('jogadorA ganhou')		
		return 'ganhadorA'
	elif vitoria5 == vitoriaB:
		print('jogadorB ganhou')
		return 'ganhadoB'
	elif vitoria6 == vitoriaA:
		print('jogadorA ganhou')		
		return 'ganhadorA'
	elif vitoria6 == vitoriaB:
		print('jogadorB ganhou')
		return 'ganhadoB'
	elif vitoria7 == vitoriaA:
		print('jogadorA ganhou')		
		return 'ganhadorA'
	elif vitoria7 == vitoriaB:
		print('jogadorB ganhou')
		return 'ganhadoB'
	elif vitoria8 == vitoriaA:
		print('jogadorA ganhou')		
		return 'ganhadorA'
	elif vitoria8 == vitoriaB:
		print('jogadorB ganhou')
		return 'ganhadoB'
	else:
		return 'continua'	
	
def ZeraTabela():
	tabela =	[
			['0','0','0'],
			['0','0','0'],
			['0','0','0']
		 ]	
	
	return tabela

	

#variaveis

tabela = ZeraTabela()
jogadorA = '1'
jogadorB = '2'
jogador = jogadorA



# while true == roda o jogoa

while True:
	user = input('posição :')	
	if user == 0:
		break
	else:
		posicao = PosicaoJogador(user)
		PreencherTabela(posicao)
		VerificarGanhador(tabela)
		jogador = TrocarJogador(jogador)
		

