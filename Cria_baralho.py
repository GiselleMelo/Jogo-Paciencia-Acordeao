def cria_baralho ():
    cartas_baralho = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']
    return cartas_baralho

mensagem = cria_baralho()
for i in range(0,len(mensagem)):
    print("A carta de indice {} é {}".format(i,mensagem[i]))

'''
precisa otimizar essa função do baralho, ta fazendo tudo na mão
'''