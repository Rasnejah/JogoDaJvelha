# encoding: utf-8

from jogoDavelha import JogoDaVelha
import os

velha = JogoDaVelha()
jogador = velha.Jogador()


while True:
	print('Vez do jogador {}'.format(jogador))
	for i in range(len(velha.matriz)):
		print(velha.matriz[i])
	user = int(input('Digite uma posição para jogar: 1 á 9 ou 0 para sair '))
	
	if user == 0 :
		break
	else:
		if jogador == 1:
			velha.PosicaoMatriz(user, 'jogadorA')
		else:
			velha.PosicaoMatriz(user, 'jogadorB')
		for i in range(len(velha.matriz)):
			print(velha.matriz[i])		
		if velha.VerificarMatriz(jogador) == jogador:
			velha.ZeraMtriz()
			sair = input('Deseja jogar novamente? S/N ')
			if sair == 'N' or sair == 'n':
				break
			else:
				continue
		jogador = velha.TrocarJogador(jogador)
		os.system('clear') or None

