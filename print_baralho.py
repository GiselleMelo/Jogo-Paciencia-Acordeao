''' 
código que a variável baralho
e devolve as cartas printadas com a respectiva ordem
'''
from colorama import Fore, Back, Style
from extrai_naipe import *

def print_baralho_ordenado(baralho):
    # variável aux para o while, i
    i = 0
    while (i < len(baralho)):
        aux = i + 1
        # variável aux para o while, i
        i = 0
        while (i < len(baralho)):
            aux = i + 1
            #print("{} - {}".format(aux,baralho[i]))
            naipe = extrai_naipe(baralho[i])
            if naipe == '♥':
                print('\033[0m' + str(i+1) + " - " + '\033[91m' + baralho[i] + '\033[0m')
            elif naipe == '♦':
                print('\033[0m' + str(i+1) + " - " + '\033[93m' + baralho[i] + '\033[0m')
            elif naipe == '♣':
                print('\033[0m' + str(i+1) + " - " + '\033[92m' + baralho[i] + '\033[0m')
            elif naipe == '♠':
                print('\033[0m' + str(i+1) + " - " + '\033[94m' + baralho[i] + '\033[0m')
            i += 1
        # a função não tem valores a retornar

