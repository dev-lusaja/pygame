import pygame


class Board:
    snake = None
    snack = None
    obstacles = None

    def __init__(self):
        self.width = 500
        self.height = 20
        self.velocity = 9
        self.initial_position = (10, 10)
        self.lines_color = (0, 50, 0)
        self.window = pygame.display.set_mode((self.width, self.width))
