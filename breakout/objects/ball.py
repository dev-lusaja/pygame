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

    def initial_position(self, board, block_size):
        position = self.calculate_position(board, block_size)
        self.rectangle.move_ip(position)

    def collide(self, axis):
        self.sound.play(0)
        self.position[axis] = -self.position[axis]

    def calculate_position(self, board, block_size):
        return randint(self.size, board.width - self.size), (block_size * board.level) + board.header + (block_size // 2)
