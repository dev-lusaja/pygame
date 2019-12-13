import pygame
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()

windows_size = 800, 600
width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ball Game')

speed = [1, 1]
color_white = 255, 255, 255

ball = pygame.image.load(os.path.join(dir_path, 'ball.png'))
ball_rect = ball.get_rect()

shoe = pygame.image.load(os.path.join(dir_path, 'shoe.png'))
shoe_rect = shoe.get_rect()
shoe_rect.move_ip(400, 300)

run = True
while run:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        shoe_rect = shoe_rect.move(0, -1)
    if keys[pygame.K_DOWN]:
        shoe_rect = shoe_rect.move(0, 1)

    if shoe_rect.colliderect(ball_rect):
        speed[0] = -speed[0]

    ball_rect = ball_rect.move(speed)

    if shoe_rect.top < 0:
        shoe_rect = shoe_rect.move(0, 1)
    if shoe_rect.bottom > height:
        shoe_rect = shoe_rect.move(0, -1)

    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color_white)
    screen.blit(ball, ball_rect)
    screen.blit(shoe, shoe_rect)
    pygame.display.flip()

pygame.quit()
