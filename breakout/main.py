import sys
import pygame

from objects.constants import COLOR_WHITE, COLOR_BLACK, COLOR_GREEN, MIN_HEIGHT
from objects.board import Board
from objects.ball import Ball
from objects.bar import Bar
from objects.block import Block
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

        wall = Wall(block)
        wall.create(board.width)

        ball = Ball()
        ball.initial_position(board.width, board.height)

        bar = Bar()
        bar.initial_position((board.width // 2, board.height - 50))

        game_over_text = Text('Game Over', COLOR_WHITE, COLOR_BLACK).center(board.width, board.height)
        pause_text = Text('Pause', COLOR_WHITE, COLOR_BLACK).center(board.width, board.height)
        win_text = Text('You win !!!', COLOR_GREEN, COLOR_BLACK).center(board.width, board.height)
        clock = pygame.time.Clock()
        while self.running:
            # fps
            clock.tick(60)

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

            if not self.pause:
                # rebound ball
                ball.rebound()

                # control ball sides
                ball.control_sides(board.width)

                # ball hit bar
                bar.hits_the_ball(ball)

                # control bar sides
                bar.control_sides(board.width)

                # ball hit the wall
                wall.collides_with_ball(ball)
                # screen
                board.screen.fill(COLOR_BLACK)

                for blck in wall.blocks:
                    board.screen.blit(block.surface, blck)

                if len(wall.blocks) == 0:
                    # win
                    board.screen.blit(win_text.surface, win_text.rectangle)
                elif ball.overshoot(board.height):
                    # game over
                    ball.rectangle.center = ball.calculate_position(board.width, board.height)
                    # board.screen.blit(game_over_text.surface, game_over_text.rectangle)

                # draw objects
                board.screen.blit(bar.surface, bar.rectangle)
                board.screen.blit(ball.surface, ball.rectangle)
            else:
                # pause
                board.screen.blit(pause_text.surface, pause_text.rectangle)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.mixer.init(22100, -16, 2, 64)  # fix for sound
    pygame.init()
    breakOut = BreakOut()
    breakOut.start()
