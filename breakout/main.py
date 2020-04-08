import sys
import pygame

from objects.constants import COLOR_WHITE, COLOR_BLACK, COLOR_GREEN, MIN_HEIGHT
from objects.board import Board
from objects.ball import Ball
from objects.bar import Bar
from objects.block import Block, BlockRed
from objects.text import Text
from objects.wall import Wall


class BreakOut:

    def __init__(self):
        pygame.mouse.set_visible(0)
        self.running = True
        self.pause = False

    def start(self):
        # Objects
        board = Board()

        block = Block()
        block_red = BlockRed()
        wall = Wall(block)
        wall.create(board)

        ball = Ball()
        ball.initial_position(board, block.size)

        bar = Bar()
        bar.initial_position((board.width // 2, board.height - 50))

        game_over_text = Text('Game Over', COLOR_WHITE, COLOR_BLACK).center(board.width, board.height)
        pause_text = Text('Pause', COLOR_WHITE, COLOR_BLACK).center(board.width, board.height)
        win_text = Text('Next Level !!!', COLOR_GREEN, COLOR_BLACK).center(board.width, board.height)
        clock = pygame.time.Clock()
        while self.running:
            # fps
            clock.tick(60)
            header_surface, header_rectangle = board.get_header()

            # screen
            board.screen.fill(COLOR_BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        bar.rectangle = bar.rectangle.move(-bar.speed, MIN_HEIGHT)
                    if event.key == pygame.K_RIGHT:
                        bar.rectangle = bar.rectangle.move(bar.speed, MIN_HEIGHT)
                    if event.key == pygame.K_SPACE:
                        self.pause = not self.pause

            if board.lives > 0:
                if not self.pause:

                    # rebound ball
                    ball.rebound()

                    # control ball sides
                    ball.control_sides(board)

                    # ball hit bar
                    bar.hits_the_ball(ball)

                    # control bar sides
                    bar.control_sides(board.width)

                    # ball hit the wall
                    if wall.collides_with_ball(ball):
                        board.score += 10

                    for block_in_wall in wall.blocks:
                        board.screen.blit(block_red.surface, block_in_wall)

                    # next level
                    if len(wall.blocks) == 0:
                        pygame.time.wait(100)
                        board.next_level()
                        ball.rectangle.center = ball.calculate_position(board, block.size)
                        wall.create(board)
                    # reduce live
                    elif ball.overshoot(board.height):
                        board.lives -= 1
                        ball.rectangle.center = ball.calculate_position(board, block.size)

                    # draw objects
                    board.screen.blit(bar.surface, bar.rectangle)
                    board.screen.blit(ball.surface, ball.rectangle)
                else:
                    # pause
                    board.screen.blit(pause_text.surface, pause_text.rectangle)
            else:
                # game over
                board.screen.blit(game_over_text.surface, game_over_text.rectangle)

            # header
            board.screen.blit(header_surface, header_rectangle)
            pygame.display.update()


if __name__ == '__main__':
    pygame.mixer.init(22100, -16, 2, 64)  # fix for sound
    pygame.init()
    breakOut = BreakOut()
    breakOut.start()
