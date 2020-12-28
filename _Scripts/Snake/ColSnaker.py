import _Scripts.Snake.Snake as SK  # importa o arquivo que contém as funções de movimento da cobra
import _Scripts.Data.Data as DT  # importa arquivo que contém os dados para o programa
import _Scripts.Fruit.Fluit as FT  # importa arquivo que contém a função que gera as posições da fruta
import _Scripts.Fruit.ColFluit as CF  # importa o arquivo que contém a função de colisão com as frutas


def ColSnaker():
    """
    Função que verifica a colisão da cobra.
    :return:
    """
    a, b = SK.snaker[-1]  # pega a última posição da lista de posições da cobra
    if a >= DT.a or a < 0 or b >= DT.a or b < 0 or SK.snaker[-1] in SK.snaker[:-2]:  # verifica colisão da cobra
        SK.Inicializalista()  # reinicia o jogo
        CF.hankingatual = 0  # zera a pontuação atual
        FT.gera = True  # permissão para gerar uma nova fruta
