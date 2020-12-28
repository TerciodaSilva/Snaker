import _Scripts.Snake.Snake as SK  # importa o arquivo que contém as funções de movimento da cobra

hankinggeral = 0  # maior pontuação do jogo
hankingatual = 0  # pontuação do jogo jogo atual


def ColisaoFluit(a, b):
    """
    Função que verifica a colisão com a fruta.
    :param a:
    :param b:
    :return:
    """
    global hankinggeral, hankingatual
    if [a, b] in SK.snaker:  # se a posição da fruta está dentro das posições das cobras
        SK.snaker.append(SK.snaker[-1])  # dublica a última posição da cobra
        hankingatual += 10  # incrementa a pontuação atual
        if hankingatual > hankinggeral:  # se a pontuação atual for maior que a pontuação geral
            hankinggeral += 10  # atualiza a pontuação geral
        return True  # valor para gerar uma nova fruta
