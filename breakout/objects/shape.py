import os

import pygame


class Shape:
    sound = None

    def __init__(self, image):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'img', 'dist', image)
        self.surface = pygame.image.load(image_path).convert_alpha()
        self.rectangle = self.surface.get_rect()

    def set_sound(self, sound):
        self.sound = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'sounds', sound))
        self.sound.set_volume(10)
