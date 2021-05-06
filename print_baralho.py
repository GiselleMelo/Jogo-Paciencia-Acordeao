''' 
código que a variável baralho
e devolve as cartas printadas com a respectiva ordem
'''

def print_baralho_ordenado(baralho):
    # variável aux para o while, i
    i = 0
    while (i < len(baralho)):
        aux = i + 1
        print("{} - {}".format(aux,baralho[i]))
        i += 1
    # a função não tem valores a retornar
