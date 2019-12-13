from objects.constants import MIN_HEIGHT, MIN_WIDTH
from objects.shape import Shape


class Ball(Shape):
    __image = 'ball.png'
    speed = 6
    position = [speed, speed]

    def __init__(self):
        Shape.__init__(self, self.__image)

    def overshoot(self, limit):
        return self.rectangle.bottom > limit

    def control_sides(self, max_width):
        if self.rectangle.left < MIN_WIDTH or self.rectangle.right > max_width:
            self.position[0] = -self.position[0]
        if self.rectangle.top < MIN_HEIGHT:
            self.position[1] = -self.position[1]

    def rebound(self):
        self.rectangle = self.rectangle.move(self.position)

    def initial_position(self, position):
        self.rectangle.move_ip(position)
