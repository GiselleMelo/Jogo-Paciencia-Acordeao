from lista_movimentos_possiveis import *

def possui_movimentos_possiveis(cartas):
    estado = False
    for i in range(0,len(cartas)):
        if len(lista_movimentos_possiveis(cartas,i)) != 0:
            #print(len(lista_movimentos_possiveis(cartas,i)))
            estado = True
    return estado 
