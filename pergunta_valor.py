# aqui será implementado o código do jogo
# vamos importar as bibliotecas criadas até agora para facilitar no processo

from Cria_baralho import *
from extrai_valor import *
from extrai_naipe import *
from lista_movimentos_possiveis import *
from Empilha_Carta import *
from Possui_movimentos_possiveis import *

# temos 52 cartas, vamos criar um contador para isso, e a medida que 
# jogamos decrementamos o contador

# vamos criar um loop para terminar o jogo ou começa-lo de novo
desejo = input(("Digite 's' para começar um jogo, para sair do jogo qualquer outra tecla "))
while (desejo == "s"):
    ### o jogo fica aqui dentro
    contador = 52
    # vamos criar o baralho a ser jogado, usando a função criar_baralho
    baralho = cria_baralho()
    print(baralho)
    # após isso devemos perguntar ao jogador um número para ser jogado
    numero = int(input("Escolha uma carta (digite um numero entre 1 e {0}) ".format(contador)))
    jogada = lista_movimentos_possiveis(baralho,numero)
