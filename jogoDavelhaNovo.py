# encoding: utf-8

import os

class JogoDaVelha:
	

	def __init__(self,):
		self.matriz = [[0,0,0],
	          		   [0,0,0],
			  		   [0,0,0]]
		self.posicao = {1:(2,0), 2:(2,1), 3:(2,2), 
						4:(1,0), 5:(1,1), 6:(1,2), 
						7:(0,0), 8:(0,1), 9:(0,2)}
		self.jogador = {'jogadorA':1, 'jogadorB':-1}

	def Jogador(self):			
		jogador = self.jogador['jogadorA']
		return jogador

	def PosicaoMatriz(self,user,jogador):
		posicao = self.jogador[jogador]
		matriz = self.matriz[self.posicao[user][0]] [self.posicao[user][1]]
		if matriz == self.jogador['jogadorA'] or matriz == self.jogador['jogadorB']:
			print('Posição já marcada, perdeu a vez')
		else:
			posicao = self.jogador[jogador]
			self.matriz[self.posicao[user][0]] [self.posicao[user][1]] = posicao

	def TrocarJogador(self,jogador):
		if jogador == self.jogador['jogadorA']:
			jogador = self.jogador['jogadorB']
			return jogador
		else:
			jogador = self.jogador['jogadorA']

			return jogador
	def VerificarMatriz(self, jogador):
		for i in range(len(self.matriz)):
			if sum(self.matriz[i]) == 3 or sum(self.matriz[i]) == -3 :
				print('Parabens {} você Venceu'.format(jogador))
				return jogador				

		if self.matriz[2][0] + self.matriz[1][1] + self.matriz[0][2] == 3 or self.matriz[2][0] + self.matriz[1][1] + self.matriz[0][2] == -3 :
			print('Parabens {} você Venceu'.format(jogador))
			return jogador		
		elif self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2] == 3 or self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2] == -3:
			print('Parabens {} você Venceu'.format(jogador))
			return jogador		
		elif self.matriz[0][0] + self.matriz[1][0] + self.matriz[2][0] == 3 or self.matriz[0][0] + self.matriz[1][0] + self.matriz[2][0] == -3 :
			print('Parabens {} você Venceu'.format(jogador))
			return jogador		
		elif self.matriz[0][1] + self.matriz[1][1] + self.matriz[2][1] == 3 or self.matriz[0][1] + self.matriz[1][1] + self.matriz[2][1] == -3 :
			print('Parabens {} você Venceu'.format(jogador))
			return jogador
		elif self.matriz[0][2] + self.matriz[1][2] + self.matriz[2][2] == 3 or self.matriz[0][2] + self.matriz[1][2] + self.matriz[2][2] == -3 :
			print('Parabens {} você Venceu'.format(jogador))
			return jogador
	def ZeraMtriz(self):
		self.matriz = [[0,0,0],[0,0,0],[0,0,0]]


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






