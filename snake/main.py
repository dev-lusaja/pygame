import pygame
import tkinter as tk
from tkinter import messagebox

from helpers import random_position
from shapes.snake import Snake
from shapes.snack import Snack
from shapes.board import Board
from shapes.obstacle import Obstacle


board = Board()


def draw_grid(w, rows, surface):
    size_btwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        #pygame.draw.line(surface, board.lines_color, (x, 0), (x, w))
        #pygame.draw.line(surface, board.lines_color, (0, y), (w, y))


def redraw_window(surface):
    surface.fill((0, 37, 0))
    board.snake.draw(surface)
    board.snack.draw(surface)
    for obstacle in board.obstacles.items:
        obstacle.draw(surface)
    draw_grid(board.width, board.height, surface)
    pygame.display.update()


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except Exception as e:
        print(e)


def main():
    board.snake = Snake(position=board.initial_position)
    board.snack = Snack(random_position(board.height, board.snake))
    board.obstacles = Obstacle()
    board.obstacles.create(10, board.snake, board.height)
    run_game = True

    clock = pygame.time.Clock()

    while run_game:
        pygame.time.delay(50)
        clock.tick(board.velocity)
        board.snake.move()
        if board.snake.body[0].pos == board.snack.pos:
            board.snake.add_cube()
            board.snack = Snack(random_position(board.height, board.snake))

        # controla el choque
        for x in range(len(board.snake.body)):
            try:
                if board.snake.body[0].pos in board.obstacles.positions:
                    raise Exception('You hit an obstacle')
                if board.snake.body[x].pos in list(map(lambda z: z.pos, board.snake.body[x + 1:])):
                    raise Exception('You Lost!')
            except Exception as e:
                print('Score:, %s' % len(board.snake.body))
                message_box('Play again...', e)
                board.snake.reset(position=board.initial_position)
                board.obstacles.create(10, board.snake, board.height)
                break
        redraw_window(board.window)


main()
