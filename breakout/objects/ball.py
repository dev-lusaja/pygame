from random import randint

from objects.constants import MIN_HEIGHT, MIN_WIDTH
from objects.shape import Shape


class Ball(Shape):
    speed = 8
    position = [speed, speed]  # x, y

    def __init__(self):
        Shape.__init__(self, 'ball.png')

    def overshoot(self, limit):
        return self.rectangle.bottom > limit

    def control_sides(self, max_width):
        if self.rectangle.left < MIN_WIDTH or self.rectangle.right > max_width:
            self.collide(0)  # x
        if self.rectangle.top < MIN_HEIGHT:
            self.collide(1)  # y

    def rebound(self):
        self.rectangle = self.rectangle.move(self.position)

    def initial_position(self, width, height):
        position = self.calculate_position(width, height)
        self.rectangle.move_ip(position)

    def collide(self, axis):
        self.position[axis] = -self.position[axis]

    @staticmethod
    def calculate_position(width, height):
        return randint(1, width), height // 3
