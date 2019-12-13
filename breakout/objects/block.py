from objects.shape import Shape


class Block(Shape):
    __image = 'block.png'

    def __init__(self):
        Shape.__init__(self, self.__image)
        self.size = self.rectangle.right - self.rectangle.left
