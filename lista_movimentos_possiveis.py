'''
Este exercício foi desenvolvido como parte do EP2 do primeiro semestre de 2021.

Implemente uma função que recebe um baralho representado como uma lista de 
strings e o índice (posição) de uma carta e devolve uma lista contendo os 
movimentos possíveis para essa carta no jogo de Paciência Acordeão. Os movimentos 
possíveis são representados pelos números 1 (a carta pode ser empilhada sobre 
seu vizinho imediatamente anterior) e 3 (a carta pode ser empilhada sobre o 
terceiro vizinho anterior).

alguns exemplos:

Se o baralho for a lista ['6♥', 'J♥', '9♣', '9♥'] e o índice for 1, sua função 
deve devolver [1], pois a carta 'J♥' possui o mesmo naipe de seu vizinho 
imediatamente anterior ('6♥');

Se o baralho for a lista ['6♥', 'J♥', '9♣', '9♥'] e o índice for 2, sua função 
deve devolver [], pois o '9♣' não pode ser empilhado sobre seu vizinho

Se o baralho for a lista ['6♥', 'J♥', '9♣', '9♥'] e o índice for 3, sua função 
deve devolver [1, 3], pois o '9♥' possui o mesmo valor de seu vizinho imediatamente 
anterior ('9♣') e o mesmo naipe de seu terceiro vizinho anterior ('6♥');

vamos usar as funções já criadas para extrair o nipe e o valor da carta

'''

def extrai_valor (b):
    carta = b
    #casos do numero ser igual a 10
    if len(carta)>2:
        num = carta[0]+carta[1]
    #outros casos
    else:
        num = carta[0]
    return num

def extrai_naipe(carta):
# a carta pode ter 3 caracteres, isso precisa ser levado em conta 
# só queremos o nipe, o último caractere
# dividindo em dois casos, temos:

    if (len(carta) == 2):
        # carta do tipo 5♠, com dois caracteres
        naipe = carta[1]
    elif (len(carta) == 3):
        # carta do tipo 10♠, com 3 caracteres
        naipe = carta[2]

    if naipe == "♠":
        return "♠"
    elif naipe == "♥":
        return "♥"
    elif naipe == "♦":
        return "♦" 
    elif naipe == "♣":
        return "♣"

def lista_movimentos_possiveis(baralho,indice):

    movimentos = []

    if indice == 0:
        # analisar a primeira carta
        # ela não tem carta anterior
        # retorna lista vazia
        return movimentos

    # se indice diferente de 0, então temos que saber
    # o nipe e o valor da carta, as linhas abaixo fazem isso
    nipe = extrai_naipe(baralho[indice])
    valor = extrai_valor(baralho[indice])
    # preciso saber as informações da carta a ser comparada
    nipe_anterior = extrai_naipe(baralho[indice - 1])
    valor_anterior = extrai_valor(baralho[indice - 1])
    # nas respectivas variaveis temos as informações necessárias

    if (len(baralho) <= 3):
        # só temos 3 cartas no baralho
        # não podemos empilhar sobre a 3 anterior,
        # pois não tem essa carta
        if ((nipe == nipe_anterior) or (valor == valor_anterior)):
            # deu bom, então podemos mover como a carta anterior
            movimentos.append(1)

    elif (len(baralho) >= 4):
        # temos 4 cartas ou mais, todos os movimentos 
        # são possíveis, temos que analizar
        # neste caso temos além do nipe anterior e valor anterior
        # também temos o caso de 3 antes
        nipe_anterior_3 = extrai_naipe(baralho[indice - 3])
        valor_anterior_3 = extrai_valor(baralho[indice - 3])

        if ((nipe == nipe_anterior) or (valor == valor_anterior)):
            # deu bom, então podemos mover como a carta anterior
            movimentos.append(1)
        if ((((nipe == nipe_anterior_3) or (valor == valor_anterior_3)) and (indice -3) >= 0)):
            # deu bom no caso da antepenultima
            movimentos.append(3)

    return movimentos