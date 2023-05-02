import pygame, sys

pygame.init()

#Colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = ( 0, 0, 255)

#Pantalla
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#Mouse
pygame.mouse.set_visible(0)

#Jugadores
player_with = 15
player_height = 90

player_one_x = 30
player_one_y = 255
player_one_speed = 0

player_two_x = 755
player_two_y = 255
player_two_speed = 0

#Pelota
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

# Bucle principal
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
    
    #Movimiento en pantalla
    if (player_one_y > 510 or player_one_y < 0):
        player_one_speed *= -1
    if (player_two_y > 510 or player_two_y < 0):
        player_two_speed *= -1

    if ball_x > 800 or ball_x < 0:
        ball_x = 400
        ball_y = 300
        ball_speed_x *= -1
        ball_speed_y *= -1
    if (ball_y > 600 or ball_y < 10):
        ball_speed_y *= -1

    player_one_y += player_one_speed
    player_two_y += player_two_speed
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    screen.fill(green)

    #Imagenes
    player_one = pygame.draw.rect(screen, black, (player_one_x, 
                                                  player_one_y, 
                                                  player_with, 
                                                  player_height))
    player_two = pygame.draw.rect(screen, black, (player_two_x, 
                                                  player_two_y, 
                                                  player_with, 
                                                  player_height))
    
    ball = pygame.draw.circle(screen, black, (ball_x, ball_y), 10)

    pygame.draw.circle(screen, white, (400, 300), 15)
    pygame.draw.line(screen, white, [400, 0], [400, 600], 5)

    #Colisiones
    if ball.colliderect(player_one) or ball.colliderect(player_two):
        ball_speed_x *= -1
    
    pygame.display.flip()
    clock.tick(60)
