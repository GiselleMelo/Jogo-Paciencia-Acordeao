import random 

def cria_baralho ():
    naipe = ['♠','♥','♦','♣']
    num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    baralho = []
    for n in range(0,len(num)):
        for i in range(0,len(naipe)):
            baralho.append(num[n]+naipe[i])
    # a função shuffle de random embaralha str
    # vamos usar ela para embaralhar o nosso deck de cartas
    random.shuffle(baralho)
    return baralho