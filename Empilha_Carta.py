def empilha(lista,origem,destino):
    lista[destino] = lista[origem]
    del lista[origem]
    return lista