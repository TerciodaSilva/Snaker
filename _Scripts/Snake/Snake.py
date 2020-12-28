import _Scripts.Data.Data as DT  # importa arquivo que contém os dados para o programa
import _Scripts.Snake.ColSnaker as CS  # importa o arquivo que contém a função de colisão da cobra
import pygame  # importa a biblioteca pygame

snaker = list()  # lista de posições da cobra
a = b = 0  # posição inicial da cobra
Inicia = False  # variável para reiniciar o jogo


def Inicializalista():
    """
    Essa função reinicia o jogo.
    :return:
    """
    global a, b, Inicia, snaker  # variáveis globais que serão modificadas
    snaker.clear()  # limpa as posições da lista
    a = b = 0  # reinicia a posição inicial da cobra
    for i in range(2):
        snaker.append([0, 0])  # duas posições inicial da cobra
    Inicia = True  # variável de reinício


Inicializalista()  # chama a inicialização do jogo


def MoveTopDown(y):
    """
    Função que movimenta a cobra no eixo das ordenadas.
    :param y:
    :return:
    """
    snaker.append([snaker[-1][0], y * DT.x])  # próxima posição para a cobra
    snaker.pop(0)  # excluí a primeira posição da lista das posições da cobra


def MoveRightLeft(x):
    """
    Função que movimenta a cobra no eixo das abscissas.
    :param x:
    :return:
    """
    snaker.append([x * DT.x, snaker[-1][1]])  # próxima posição para a cobra
    snaker.pop(0)  # excluí a primeira posição da lista das posições da cobra


def MoveSnaker(screen):
    """
    Cria e movimenta os bloco do corpo da cobra pela tela.
    :param screen: Tela que será exibido.
    :return:
    """
    for i in snaker:
        x, y = i  # posições de um dos blocos da cobra
        pygame.draw.rect(screen, DT.CorBlack, (x, y, DT.x, DT.x))  # desenha os blocos da cobra em tela
        CS.ColSnaker()  # verifica se ouve colisão
