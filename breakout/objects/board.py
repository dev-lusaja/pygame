import pygame


class Board:
    width, height = 400, 650
    __title = 'BreakOut'

    def __init__(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.__title)
