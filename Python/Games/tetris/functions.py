import pygame
import sys
import os
from time import time
import classes
import globals

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def total_time(start_time):
    return time() - start_time

def speed(time):
    a = 400
    k = 0.01
    return a * 2.71828 ** (-1 * k * time)

def handle_completed_rows(floor):
    for row in range(19, -1, -1):
        completed = True
        for column in range(10):
            if [column, row] not in floor:
                completed = False
        if completed:
            for column in range(10): floor.remove([column, row])
            # Now, for all the rows above this completed row, drop the y by 1
            for index in range(len(floor)):
                if floor[index][1] < row: floor[index][1] += 1
            return True
    return False

def displayScoreboard(screen, time, num_objects):
    #Create a division between scoreboard and the playing board
    bottomRect = pygame.Rect(0, 20 * globals.grid_width, 10 * globals.grid_width, 5)
    leftRect = pygame.Rect(0, 0, 5, 20 * globals.grid_width)
    rightRect = pygame.Rect(10 * globals.grid_width - 5, 0, 5, 20 * globals.grid_width)
    topRect = pygame.Rect(0, 0, 10 * globals.grid_width, 5)
    pygame.draw.rect(screen, (255, 255, 255), bottomRect)
    pygame.draw.rect(screen, (255, 255, 255), topRect)
    pygame.draw.rect(screen, (255, 255, 255), leftRect)
    pygame.draw.rect(screen, (255, 255, 255), rightRect)

    #Display the text of the score
    font_file_path = resource_path(os.path.join("data", "freesansbold.ttf"))
    font = pygame.font.Font(font_file_path, (int)(round(1 * globals.grid_width)))
    time_str = "Time: " + (str)(round(time, 1)) + " Seconds"
    count_str = "Count: " + (str)(num_objects)
    time_text = font.render(time_str, True, (255, 255, 255))
    count_text = font.render(count_str, True, (255, 255, 255))
    time_rect = time_text.get_rect()
    count_rect = count_text.get_rect()
    time_rect.center = (5 * globals.grid_width, 21.75 * globals.grid_width)
    count_rect.center = (5 * globals.grid_width, 23.5 * globals.grid_width)
    screen.blit(time_text, time_rect)
    screen.blit(count_text, count_rect)

def displayGameOver(screen):
    font_file_path = resource_path(os.path.join("data", "freesansbold.ttf"))
    font = pygame.font.Font(font_file_path, (int)(round(globals.grid_width * 2.5)))
    game_text = font.render("GAME", True, (150, 0, 0))
    over_text = font.render("OVER", True, (150, 0, 0))
    game_rect = game_text.get_rect()
    over_rect = over_text.get_rect()
    game_rect.center = (5 * globals.grid_width, 8.5 * globals.grid_width)
    over_rect.center = (5 * globals.grid_width, 11 * globals.grid_width)
    screen.blit(game_text, game_rect)
    screen.blit(over_text, over_rect)

def displayFloor(screen, floor):
    for point in floor:
        upperLeft = getUpperLeft(point)
        pygame.draw.rect(screen, (100,10,100), pygame.Rect(upperLeft[0], upperLeft[1], globals.shape_width, globals.shape_width))

def displayShape(screen, shape):
    tempList = shape.get_object_list()
    for point in shape.get_object_list():
        upperLeft = getUpperLeft(point)
        pygame.draw.rect(screen, shape.get_color(), pygame.Rect(upperLeft[0], upperLeft[1], globals.shape_width, globals.shape_width))

def getUpperLeft(point):
    return [point[0] * globals.grid_width + (globals.grid_width - globals.shape_width) / 2, point[1] * globals.grid_width + (globals.grid_width - globals.shape_width) / 2]