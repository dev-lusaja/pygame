from helpers import random_position
from .cube import Cube


class Obstacle:
    color = (138, 58, 11)
    items = []
    positions = []

    def create(self, cant, snake, height):
        self.positions.clear()
        self.items.clear()
        for number in range(1, cant):
            obstacle = Cube(random_position(height, snake), color=self.color)
            #self.items.append(obstacle)
            #self.positions.append(obstacle.pos)
