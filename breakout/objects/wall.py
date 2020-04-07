
class Wall:
    blocks = []

    def __init__(self, block):
        self.block = block

    def create(self, board):
        self.blocks = []
        x, y = 0, board.header
        cant = (board.width // self.block.size) * board.level
        for block in range(cant):
            if x == board.width:
                x = 0
                y += self.block.size
            self.blocks.append(self.block.rectangle)
            self.blocks[block] = self.blocks[block].move(x, y)
            x += self.block.size
        return self.blocks

    def collides_with_ball(self, ball):
        index = ball.rectangle.collidelist(self.blocks)
        if index != -1:
            if self.blocks[index].left > ball.rectangle.center[0] or \
                    self.blocks[index].right < ball.rectangle.center[0]:
                ball.collide(0)  # x
                ball.collide(1)  # y
            else:
                ball.collide(1)  # y
            del self.blocks[index]
            return True
