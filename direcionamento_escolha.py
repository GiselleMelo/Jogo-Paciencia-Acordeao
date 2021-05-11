'''
função para direcionar a escolha do usuario
temos 3 opções
1 - o usuario escolher uma carta que não pode ser jogada
2 - escolher uma carta que pode ser movida de uma maneira
3 - o usuario escolher uma carta que pode ser movida de 2 maneiras
'''
from Empilha_Carta import *
from print_baralho import *
from extrai_naipe import *

def direcionamento_escolha_usuario(numero,possiveis,baralho):
    # a função recebe o numero digitado pelo usuario
    # um vetor de até 2 posições
    # se tem nenhuma possição não é possível jogar
    # se tem uma posição, só é posível realizar uma jogada
    # se tem 2 possições temos 2 jogadas posíveis
    # e também recebe o baralho até então

    if (len(possiveis) == 0):
        # caso em que o usuario escolher um movimento impossível
        print("Você escolheu uma jogada impossível")
        return False

    elif (len(possiveis) == 1):
        # tem exatamente uma jogada possível, vamos executa-la 
        # primeiro vamos definir o indice do destino
        # se possiveis = 1, então na carta anterior
        # se possiveis = 3, então na antepenultima
        if (possiveis[0] == 1):
            destino = numero - 2
            # -2 porque o primeiro menos 1 é para tornar o número do usuário igual ao indice 
            # o segundo -1 para realmente dizer o destino da carta
            # agora invocamos a função empilha
            # lembrando que o segundo argumento precisa ser decrementado, pois ele é um valor
            # acima do indice usado no código
        else:
            # quer dizer que a jogada é na antepenultima, logo o destino é 3 cartas atrás
            destino = numero - 4
            # o porquê do -4 segue a mesma lógica supracitada do caso anterior
        ########## saindo do condicional do destino###########
        # implementamos o empilhamento do baralho invocando a função empilha
        empilha(baralho, numero - 1, destino)
        print_baralho_ordenado(baralho) 
        return True
    else:
        # se estamos nesse condicinal quer dizer que temos 2 jogadas possíveis
        # preciamos perguntar ao usuario qual jogada ele quer realizar
        # para printar a infamação das possíveis cartas vamos guardar em um vetor das cartas possíveis
        possibilidades = [baralho[numero - 2],baralho[numero - 4]]
        while True:
                # vamos estrair o naipe de cada carta da possibilidade para colocar a cor correta no print
                nipe_1 = extrai_naipe(possibilidades[0])
                nipe_2 = extrai_naipe(possibilidades[1])
                # de posse dos nipes podemos printar com as cores adequadas
                # com um for alinhado vamos descobrir qual caso a ser printado
                naipes = ['♠','♥','♦','♣']
                c1 = ""
                c2 = ""
                i = 0
                while i in range(0,len(naipes)):
                    if naipes[i] == nipe_1:
                        # achamos o nipe da primeira carta
                        # de acordo com o indice temos o nipe, logo a cor
                        if i == 0:
                            #spada
                            c1 = '\033[94m'
                        elif i == 1:
                            #copas
                            c1 = '\033[91m'
                        elif i == 2:
                            #ouros
                            c1 = '\033[93m'
                        elif i == 3:
                            #paus
                            c1 = '\033[92m'
                    if naipes[i] == nipe_2:
                        # achamos o nipe da segunda carta
                        # de acordo com o indice temos o nipe, logo a cor
                        if i == 0:
                            #spada
                            c2 = '\033[94m'
                        elif i == 1:
                            #copas
                            c2 = '\033[91m'
                        elif i == 2:
                            #ouros
                            c2 = '\033[93m'
                        elif i == 3:
                            #paus
                            c2 = '\033[92m'
                    i += 1
                # já temos todos os nipes salvos
                # agora vamos determinar a cor, testando os nipes
                numero2 = int(input("\033[0m" + "Escolha onde empilhar: \n1 - " + c1 + "{}".format(possibilidades[0]) + "\033[0m" + " ou\n2 - "+ c2 + "{}".format(possibilidades[1]) + "\033[0m" + "\nResposta:"))
                if numero2!=1 and numero2!=2:
                    print("Jogada inválida! \n Digite outro valor!")
                else:
                    empilha(baralho, int(numero)-1, int(numero)-1-numero2)
                    print_baralho_ordenado(baralho)
                    break
        return True        