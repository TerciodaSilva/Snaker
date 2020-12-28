import _Scripts.Data.Data as DT  # importa arquivo que contém os dados para o programa
import _Scripts.Fruit.Fluit as RF  # importa o arquivo que contém a função que gera um fruta em tela
import _Scripts.Snake.Snake as SK  # importa o arquivo que contém as funções de movimento da cobra
import _Scripts.RenderText.ScreenText as ST  # importa o arquivo que contém a função renderiza os textos em tela
import _Scripts.Fruit.ColFluit as CF  # importa o arquivo que contém a função de colisão com as frutas
import pygame  # importa a biblioteca pygame

pygame.init()  # inicializa o pygame
top, down, left, right = False, False, False, True  # inicializa o movimento da cobra para à direita

while True:
    screen = pygame.display.set_mode(DT.dimensions)  # cria a janela do jogo
    pygame.display.set_caption("Snake")  # texto da janela do jogo
    screen.fill(DT.CorWhite)  # cor do fundo da janela do jogo

    if pygame.key.get_pressed()[pygame.K_SPACE]:  # evento da tecla espaço do teclado
        retorno = False  # variável de flag para que o evento do teclado despause apenas na segunda interação do loop
        while True:
            if pygame.event.get(pygame.QUIT):  # evento para fechar a janela do jogo
                pygame.quit()  # encerra o pygame
                exit(0)  # finaliza o programa

            pause = ST.Screen_Text("Pause", 100)  # texto que será impresso em tela
            screen.blit(pause, ((DT.a / 2) - 100, (DT.a / 2) - 100))  # exibe o texto em tela
            mensagem = ST.Screen_Text("Pressione Space para continuar", 30)  # texto que será impresso em tela
            screen.blit(mensagem, ((DT.a / 2) - 150, (DT.a / 2)))  # exibe o texto em tela

            pygame.display.update()  # atualiza os elementos em tela

            pygame.time.delay(100)

            if pygame.key.get_pressed()[pygame.K_SPACE] and retorno:  # evento da tecla espaço do teclado
                break  # interrompe o loop, saindo do pause

            retorno = True  # marca o fim da primeira interação do loop

    if pygame.key.get_pressed()[pygame.K_UP] and not down:  # evento do teclado up e se a down não estive ativada
        right, left, down, top = False, False, False, True  # atualiza as variáveis de movimento

    elif pygame.key.get_pressed()[pygame.K_DOWN] and not top:  # evento do teclado down e se a up não estive ativada
        right, left, down, top = False, False, True, False  # atualiza as variáveis de movimento

    elif pygame.key.get_pressed()[pygame.K_RIGHT] and not left or SK.Inicia:  # evento do teclado right e se a left
        # não estive ativada ou reinício do jogo
        right, left, down, top = True, False, False, False  # atualiza as variáveis de movimento
        SK.Inicia = False  # desativa o evento de início do jogo

    elif pygame.key.get_pressed()[pygame.K_LEFT] and not right:  # evento do teclado left e se a right não estive
        # ativada
        right, left, down, top = False, True, False, False  # atualiza as variáveis de movimento

    if top:  # movimento para cima
        SK.a -= 1  # sobe no eixo das ordenadas
        SK.MoveTopDown(SK.a)  # atualiza as posições dos bloco da cobra
    if down:  # movimento para baixo
        SK.a += 1  # desce no eixo das ordenadas
        SK.MoveTopDown(SK.a)  # atualiza as posições dos bloco da cobra
    if left:  # movimento para baixo
        SK.b -= 1  # move-se para esquerda no eixo das abscissas
        SK.MoveRightLeft(SK.b)  # atualiza as posições dos bloco da cobra
    if right:  # movimento para baixo
        SK.b += 1  # move-se para direita no eixo das abscissas
        SK.MoveRightLeft(SK.b)  # atualiza as posições dos bloco da cobra

    if pygame.event.get(pygame.QUIT):  # evento para fechar a tela do jogo
        pygame.quit()  # encerra o pygame
        exit(0)  # finaliza o programa

    scope = ST.Screen_Text("Melhor Pontuação: " + str(CF.hankinggeral), 20)  # texto para ser impresso em tela
    scopeatual = ST.Screen_Text("Pontuação Atual: " + str(CF.hankingatual), 20)  # texto para ser impresso em tela
    mensagempause = ST.Screen_Text("Pressione Space para pausar", 20)  # texto para ser impresso em tela
    screen.blit(scope, (10, 10))  # exibe texto em tela
    screen.blit(scopeatual, (DT.a - 150, 10))  # exibe texto em tela
    screen.blit(mensagempause, ((DT.a / 3), DT.a - 20))  # exibe texto em tela

    fruit = RF.RandowFruit(screen)  # atualiza a posição da fruta na tela
    SK.MoveSnaker(screen)  # atualiza a posição da cobra na tela

    pygame.time.delay(75)
    pygame.display.update()  # atualiza a tela do jogo
