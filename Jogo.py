# aqui será implementado o código do jogo
# vamos importar as bibliotecas criadas até agora para facilitar no processo

from Cria_baralho import *
from extrai_valor import *
from extrai_naipe import *
from lista_movimentos_possiveis import *
from Empilha_Carta import *
from Possui_movimentos_possiveis import *
from print_baralho import *
from direcionamento_escolha import *
#importa a biblioteca de cores
#from colorama import Fore, Back, Style

# temos 52 cartas, vamos criar um contador para isso, e a medida que 
# jogamos decrementamos o contador
# iniciando o jogo com as perguntas

print('\nPaciência Acordeão') 
print ('================== ')
print('\nSeja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')

print('Existem apenas dois movimentos possíveis:')

print('\n1. Empilhar uma carta sobre a carta imediatamente anterior;')
print('2. Empilhar uma carta sobre a terceira carta anterior.') 

print('\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:')

print('\n1. As duas cartas possuem o mesmo valor ou ')
print('2. As duas cartas possuem o mesmo naipe.')

print('\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')

# vamos criar um loop para terminar o jogo ou começa-lo de novo
desejo = input("Aperte [Enter] para iniciar o jogo... ")
while (desejo == ""):
    ### o jogo fica aqui dentro
    contador = 52
    # vamos criar o baralho a ser jogado, usando a função criar_baralho
    baralho = cria_baralho()
    # vamos chamar a função para printar o baralho ordenado
    print_baralho_ordenado(baralho)
    # após isso devemos perguntar ao jogador um número para ser jogado
    while True:
        if len(baralho) == 1:
            print("VOCÊ VENCEU O JOGO!")
            break
        if possui_movimentos_possiveis(baralho) == False:
            print("VOCÊ PERDEU!")
            break
        numero = int(input("Escolha uma carta (digite um numero entre 1 e {0}) ".format(contador)))
        jogada_possiveis = lista_movimentos_possiveis(baralho,numero)
        direcionamento_escolha_usuario(numero, jogada_possiveis, baralho)
        contador -= 1
        
    desejo = input("Aperte [Enter] para iniciar o jogo... ")

    
