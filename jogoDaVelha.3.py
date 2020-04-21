# encoding: utf-8

''' ///////////////// descrição da atualiçãoc ///////////////

inclui as variaveis jogadorA e jogadorB , a variavel jogador altera um pelo outro


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
		tabela[posicaoTabelaL][posicaoTabelaC] = jogador

		for x in range(len(tabela)):
			print(tabela[x])
		
	else:
		print('Posição nao é valicada, digite um número de 1 a 9')
tabela = [
			['0','0','0'],
			['0','0','0'],
			['0','0','0']
		 ]
#variaveis
jogadorA = 'x'
jogadorB = '0'
jogador = jogadorA



# while true == roda o jogoa

while True:
	user = input('posição :')
	#posicao = input('digite posição')
	if user == 0:
		break
	else:
		PosicaoJogador(user)

