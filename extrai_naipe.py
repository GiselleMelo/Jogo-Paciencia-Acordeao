''' recebe uma str do tipo
    4♠
    numero acompanhado do tipo da carta
    função deve retornar o naipe da carta
'''

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
    
