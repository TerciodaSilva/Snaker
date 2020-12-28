import _Scripts.Data.Data as DT  # importa as dimesões e dados que serão utilizados no projeto.
import pygame # importa a biblioteca pygame


def Screen_Text(text, size):
    """
    Essa função permite configurar um texto de forma que ele possa ser impresso em tela, retornando o texto que será
    impresso.
    :param text:
    :param size:
    :return Screentext:
    """

    pygame.font.init()  # inicializa as fontes do pygame.
    Font = pygame.font.get_default_font()  # instancia a fonte padrão do pygame.
    Fontsystem = pygame.font.SysFont(Font, size)  # define a fonte e o tamanho dessa.
    Screentext = Fontsystem.render(text, True, DT.CorBlack)  # renderiza a fonte e a cor dessa.
    return Screentext  # retorna o texto.
