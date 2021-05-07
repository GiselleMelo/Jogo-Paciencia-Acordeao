# aqui será implementado o código do jogo
# vamos importar as bibliotecas criadas até agora para facilitar no processo

from Cria_baralho import *
from extrai_valor import *
from extrai_naipe import *
from lista_movimentos_possiveis import *
from Empilha_Carta import *
from Possui_movimentos_possiveis import *
from print_baralho import *
#importa a biblioteca de cores
from colorama import Fore, Back, Style

# temos 52 cartas, vamos criar um contador para isso, e a medida que 
# jogamos decrementamos o contador

# iniciando o jogo com as perguntas
print('Paciência Acordeão') 
print ('================== ')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')

print('Existem apenas dois movimentos possíveis:')

print('1. Empilhar uma carta sobre a carta imediatamente anterior;')
print('2. Empilhar uma carta sobre a terceira carta anterior.1) 

print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:')

print('1. As duas cartas possuem o mesmo valor ou ')
print('2. As duas cartas possuem o mesmo naipe.')

print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')

print('Aperte [Enter] para iniciar o jogo...')

# vamos criar um loop para terminar o jogo ou começa-lo de novo
baralho = cria_baralho()
while possui_movimentos_possiveis(baralho):
    ### o jogo fica aqui dentro
    contador = 52
    # vamos chamar a função para printar o baralho ordenado
    print_baralho_ordenado(baralho)
    # após isso devemos perguntar ao jogador um número para ser jogado
    numero = int(input("Escolha uma carta (digite um numero entre 1 e {0}) ".format(contador)))
    jogada_possiveis = lista_movimentos_possiveis(baralho,numero)
    print(jogada_possiveis)

termina = input('Você perdeu o jogo, deseja reiniciar?')
if termina== 'sim':
    baralho = cria_baralho()
