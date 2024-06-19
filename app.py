import os

from modelos.restaurante import RESTAURANTE
from modelos.avaliacao import AVALIACAO


def CADRASTAR():
    resname = input('Digite o nome do Restaurante: ')
    rescategoria = input('digite a Categoria do Restaurante: ')

    novores = RESTAURANTE(resname, rescategoria)
    RESTAURANTE.Restaurantes.append(novores)
    print(RESTAURANTE.LSITAR())
    CADRASTAR()



if __name__ == '__main__':
    CADRASTAR()