import pygame

from objects.text import Text
from objects.constants import COLOR_WHITE, COLOR_BLACK


class Board:
    width, height = 400, 650
    header = 20
    level = 1
    __lives = 3
    __score = 0
    __title = 'BreakOut'

    def __init__(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.__title)

    def next_level(self):
        self.level += 1

    def restart(self):
        self.level = 1

    def get_header(self):
        header_label = Text('Level: %s      Score: %d      Lives: %d' % (self.level, self.score, self.lives),
                            COLOR_WHITE, COLOR_BLACK, 12)
        header_label.rectangle.center = self.width // 2, self.header // 2
        return header_label.surface, header_label.rectangle

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, lives):
        self.__lives = lives

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score
