from random import randint
from time import sleep

import pygame

from objects.constants import MIN_WIDTH, MIN_HEIGHT
from objects.shape import Shape


class Bar(Shape):
    __image = 'bar.png'
    speed = 30

    def __init__(self):
        Shape.__init__(self, self.__image)
        pygame.key.set_repeat(1, self.speed)

    def initial_position(self, position):
        self.rectangle.move_ip(position)

    def hits_the_ball(self, ball):
        # ball hit bar
        if self.rectangle.colliderect(ball.rectangle) == 1:
            if self.rectangle.topleft > ball.rectangle.bottomright:
                ball.position[0] = -ball.position[0] + 2
            elif self.rectangle.topright < ball.rectangle.bottomleft:
                ball.position[0] = -ball.position[0] + 2
            elif self.rectangle.y > ball.rectangle.y:
                ball.position[1] = -ball.position[1]

    def control_sides(self, max_width):
        if self.rectangle.left < MIN_WIDTH:
                self.rectangle = self.rectangle.move(self.speed, MIN_HEIGHT)
        if self.rectangle.right > max_width:
            self.rectangle = self.rectangle.move(-self.speed, MIN_HEIGHT)