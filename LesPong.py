import pygame
import sys

pygame.init()

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = ( 0, 0, 255)

#Screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#Media
background = pygame.image.load("media/grass.jpg").convert()
player_image = pygame.image.load("media/pill_black.png").convert_alpha()
player_image.set_colorkey([255, 255, 255])
ball_image = pygame.image.load("media/ball_metal.png").convert_alpha()
ball_image.set_colorkey([255, 255, 255])

#Mouse
pygame.mouse.set_visible(0)

#Players
player_with = 15
player_height = 90

player_one_x = 30
player_one_y = 255
player_one_speed = 0

player_two_x = 755
player_two_y = 255
player_two_speed = 0

#Ball
ball_width = 30
ball_height = 30
ball_x = (800 - ball_width) // 2
ball_y = (600 - ball_height) // 2
ball_speed_x = 3
ball_speed_y = 3

#Main loop
while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        
        #Acción del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_one_speed = -3
            if event.key == pygame.K_s:
                player_one_speed = 3
            if event.key == pygame.K_UP:
                player_two_speed = -3
            if event.key == pygame.K_DOWN:
                player_two_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_one_speed = 0
            if event.key == pygame.K_s:
                player_one_speed = 0
            if event.key == pygame.K_UP:
                player_two_speed = 0
            if event.key == pygame.K_DOWN:
                player_two_speed = 0
    
    #Screen movements
    if (player_one_y >= 510 or player_one_y <= 0):
        player_one_speed *= -1
    if (player_two_y > 510 or player_two_y < 0):
        player_two_speed *= -1

    if ball_x >= 770 or ball_x <= 0:
        ball_x = (800 - ball_width) // 2
        ball_y = (600 - ball_height) // 2
        ball_speed_x *= -1
        ball_speed_y *= -1
    if (ball_y > 570 or ball_y < 10):
        ball_speed_y *= -1

    player_one_y += player_one_speed
    player_two_y += player_two_speed
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    #Draw area
    screen.blit(background, [0, 0])
    pygame.draw.circle(screen, white, (400, 300), 15)
    pygame.draw.line(screen, white, [400, 0], [400, 600], 5)
    ball = screen.blit(ball_image, (ball_x, ball_y))
    player_one = screen.blit(player_image, (player_one_x, player_one_y))
    player_two = screen.blit(player_image, (player_two_x, player_two_y))

    #Collisions
    if ball.colliderect(player_one) or ball.colliderect(player_two):
        ball_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)
