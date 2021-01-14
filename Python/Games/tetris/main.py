import pygame
from copy import deepcopy
from time import time

import globals
from classes import *
from functions import *

pygame.init()

x_screen = 10 * globals.grid_width
y_screen = 25 * globals.grid_width
screen = pygame.display.set_mode((x_screen, y_screen))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
start_time = time()
end_time = 0
timer = 0
num_objects = 1

shape = Random_New_Shape()
floor = []

done = False
paused = False
quit = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if not paused: paused = True
            else: paused = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if not shape.hitTheRightSide(floor): shape.set_shift(1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if not shape.hitTheLeftSide(floor): shape.set_shift(-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            temp_shape = deepcopy(shape)
            temp_shape.rotate()
            if not (temp_shape.brokeTheLeftSide(floor) or temp_shape.brokeTheRightSide(floor)): shape.rotate()

    if paused: continue

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        timer = 0

    screen.fill((0, 0, 0))
    displayShape(screen, shape)
    displayFloor(screen, floor)
    displayScoreboard(screen, total_time(start_time), num_objects)
    pygame.display.flip()

    if timer == 0 or timer > speed(total_time(start_time)):

        if shape.hitTheBottom(floor):
            # stop the shape when it hits the bottom
            for point in shape.get_object_list(): floor.append(point)

            # delete completed rows
            while handle_completed_rows(floor):
                continue

            # Check if game is over
            for point in floor:
                if point[1] < 0:
                    print("Game Over: ", total_time(start_time), " seconds")
                    end_time = total_time(start_time)
                    done = True
                    break

            # throw a new object
            shape = Random_New_Shape()
            num_objects += 1
            continue
        else:
            shape.fall()

        timer = 0

    if not paused: timer += clock.tick(60)

floor = []
done = False
while not (done or quit):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((0, 0, 0))
    displayShape(screen, shape)
    #displayFloor(screen, floor)
    displayScoreboard(screen, end_time, num_objects)
    displayGameOver(screen)
    pygame.display.flip()

    if timer == 0 or timer > 5:

        if shape.hitTheBottom(floor):
            # throw a new object
            shape = Random_New_Shape()
            continue
        else:
            shape.fall()

        timer = 0

    timer += clock.tick(60)
