import _Scripts.Data.Data as DT  # importa arquivo que contém os dados para o programa
import _Scripts.Fruit.ColFluit as CF  # importa o arquivo que contém a função de colisão com as frutas
import pygame  # importa a biblioteca pygame
from random import randint  # importa o método randint da biblioteca random

a = b = 0  # posição inicial da fruta
gera = True  # permissão para gerar um fruta


def RandowFruit(screen):
    """
    Desenha a fruta em tela.
    :param screen:
    :return:
    """
    global a, b, gera  # variáveis globais que serão modificadas
    if gera:  # se tiver permissão para gera uma fruta
        a = randint(0, (int(DT.a / DT.x) - 1))  # posição em x da fruta
        b = randint(0, (int(DT.a / DT.x) - 1))  # posição em y da fruta
        gera = False  # desativa a permissão de gerar uma fruta
    pygame.draw.rect(screen, DT.CorRed, (a * DT.x, b * DT.x, DT.x, DT.x))  # desenha a fruta em tela
    gera = CF.ColisaoFluit(a * DT.x, b * DT.x)  # verifica colisões com a fruta
