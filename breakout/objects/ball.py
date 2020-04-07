from random import randint

from objects.constants import MIN_HEIGHT, MIN_WIDTH
from objects.shape import Shape


class Ball(Shape):
    speed = 6
    position = [speed, speed]  # x, y

    def __init__(self):
        Shape.__init__(self, 'ball.png')
        self.set_sound('ballCollide.wav')

    def overshoot(self, limit):

        return self.rectangle.bottom > limit

    def control_sides(self, board):
        if self.rectangle.left < MIN_WIDTH or self.rectangle.right > board.width:
            self.collide(0)  # x
        elif self.rectangle.top < board.header:
            self.collide(1)  # y

    def rebound(self):
        self.rectangle = self.rectangle.move(self.position)

    def initial_position(self, width, height):
        position = self.calculate_position(width, height)
        self.rectangle.move_ip(position)

    def collide(self, axis):
        self.sound.play(0)
        self.position[axis] = -self.position[axis]

    @staticmethod
    def calculate_position(width, height):
        return randint(20, width - 20), height // 3
