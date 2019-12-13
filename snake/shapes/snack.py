from .cube import Cube


class Snack(Cube):
    color = (201, 0, 0)

    def __init__(self, position):
        super(Snack, self).__init__(position, color=self.color)
