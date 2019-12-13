

class Wall:
    blocks = []

    def __init__(self, block):
        self.block = block

    def create(self, width):
        self.blocks = []
        x = 0
        y = 0
        cant = width // self.block.size
        for block in range(0, cant):
            self.blocks.append(self.block.rectangle)
            if block == 0:
                self.blocks[block] = self.blocks[block].move(x, y)
            else:
                self.blocks[block] = self.blocks[block].move(x + block, y)
            x += self.block.size
        return self.blocks

    def collides_with_ball(self, ball):
        index = ball.rectangle.collidelist(self.blocks)
        if index != -1:
            if self.blocks[index].left > ball.rectangle.center[0] or \
                    self.blocks[index].right < ball.rectangle.center[0]:
                # rebound ball
                ball.position[0] = -ball.position[0]
            else:
                ball.position[1] = -ball.position[1]
            self.blocks[index:index + 1] = []
