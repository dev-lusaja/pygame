import pygame


class Text:
    def __init__(self, text, font_color, background_color, size=32):
        font = pygame.font.Font('freesansbold.ttf', size)
        self.surface = font.render(text, True, font_color, background_color)
        self.rectangle = self.surface.get_rect()

    def center(self, width, height):
        self.rectangle.center = (width // 2, height // 2)
        return self
