import pygame
import os
import math as m
import random as r

import functions
import classes

pygame.init()
time_elapsed_since_last_obstacle = 0
dt = 700

x_screen = 400
y_screen = 300
screen = pygame.display.set_mode((x_screen,y_screen))
done = False
clock = pygame.time.Clock()

_image_library = {}
def get_image(path):
    path = path.lower()
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

WHITE = (255,255,255)
image_bird = get_image("bird.png")
image_bird.set_colorkey(WHITE)

x_bird = 30
y_bird = 135
vy_bird = 0
v_max = 3
g = -.1

obstacles = []
v_obstacle = 4
width_obstacle = 10


score = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            obstacles = []
            y_bird = 135
            vy_bird = 0
            print("Score: ",score)
            score = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            vy_bird += 3
            if vy_bird > v_max: vy_bird = v_max
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("Score: ",score)
            done = True


    screen.fill((255,200,255))
    screen.blit(pygame.transform.scale(get_image("background.png"), (x_screen,y_screen)), (0,0))
    screen.blit(pygame.transform.scale(get_image("bird.png"), (40,30)), (x_bird,y_bird))
    
    if time_elapsed_since_last_obstacle > dt:
        width = r.randrange(70,120)
        y = r.randrange(20,160)
        obstacles.append(classes.obstacle(x_screen,y,y+width))
        time_elapsed_since_last_obstacle = 0

    for obstacle in obstacles:
        obstacle.x = obstacle.x - v_obstacle
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(obstacle.x, 0, width_obstacle, obstacle.y1))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(obstacle.x, obstacle.y2, width_obstacle, y_screen - obstacle.y2))

        if abs((x_bird+20)-(obstacle.x+width_obstacle/2))<(width_obstacle/2)+17.5:
            if (y_bird+15) < obstacle.y1 or (y_bird+15) > obstacle.y2:
                obstacles = []
                y_bird = 135
                vy_bird = 0
                print("Score: ",score)
                score = 0

        if obstacle.x < 0:
            obstacles.remove(obstacle)
            score += 1

    pressed = pygame.key.get_pressed()

    vy_bird = vy_bird + g
    y_bird = y_bird - vy_bird
    
    if (y_bird+15) > y_screen:
        obstacles = []
        y_bird = 135
        vy_bird = 0
        print("Score: ",score)
        score = 0

    if (y_bird+15) < 0: vy_bird = -15

    pygame.display.flip()
    time_elapsed_since_last_obstacle += clock.tick(60)
