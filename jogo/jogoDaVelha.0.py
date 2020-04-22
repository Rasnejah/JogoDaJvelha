# encoding: utf-8
''' //////////////// descrição da Verção //////////////

		pela digitação da posição que o jogador deseja marcar e dado uma tupla que
		dá as cordenadas para a posição na tabela

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
	tabela = [
			['0','0','0'],
			['0','0','0'],
			['0','0','0']
		 ]
	
	if posicao in posicaoLC:		
		print(posicaoLC[posicao])

	else:
		print('Posição nao é valicada, digite um número de 1 a 9')


while True:
	user = input('posição :')
	#posicao = input('digite posição')
	if user == 0:
		break
	else:
		PosicaoJogador(user)