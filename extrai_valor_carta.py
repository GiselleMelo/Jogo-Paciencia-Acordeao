def extrai_valor (b):
    carta = b
    if len(carta)>2:
        num = carta[0]+carta[1]
    else:
        num = carta[0]
    return num