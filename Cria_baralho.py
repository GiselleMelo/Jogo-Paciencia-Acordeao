import random 

def cria_baralho ():
    naipe = ['♠','♥','♦','♣']
    num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    baralho = []
    for n in range(0,len(num)):
        for i in range(0,len(naipe)):
            baralho.append(num[n]+naipe[i])
    
    random.shuffle(baralho)
    return baralho

b = cria_baralho()
print(b)

