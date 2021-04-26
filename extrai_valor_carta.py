#define a função
def extrai_valor (b):
    carta = b
    #casos do numero ser igual a 10
    if len(carta)>2:
        num = carta[0]+carta[1]
    #outros casos
    else:
        num = carta[0]
    return num