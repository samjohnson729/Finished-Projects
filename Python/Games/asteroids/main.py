import pygame
import os
import math as m
import random as r

import functions
import classes

pygame.init()
t = 0
dt = 2 #[ms]
ticked = False

#SETTING UP TEXT
font = pygame.font.Font(None,72)
text_end = font.render("GAME OVER", True, (255,255,255))

x_screen = 1300
y_screen = 700
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

size_rocket = 15
x_rocket = int(x_screen / 2)
y_rocket = int(y_screen / 2)
vx_rocket = 0
vy_rocket = 0

asteroid_spawn_buffer = 200

F = 2
c = .07
v_max = 150
size_missile = 5
v_missile = 35
size_bomb = 15
v_bomb = 5

asteroids = []
missiles = []
bombs = []
score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #ADDING MORE ASTEROIDS
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            okay = False
            while not okay:
                x_asteroid = r.randrange(0,x_screen)
                y_Asteroid = r.randrange(0,y_screen)
                if functions.distance( [x_asteroid, y_asteroid], [x_rocket, y_rocket] ) > asteroid_spawn_buffer: okay = True
            asteroids.append(classes.asteroid(r.randrange(24,100), [x_asteroid, y_asteroid], [r.randrange(-4,5),r.randrange(-4,5)]))

        #FIRING MISSILES
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            angle = m.atan2( (pygame.mouse.get_pos()[1] - y_rocket) , (pygame.mouse.get_pos()[0] - x_rocket) )
            missiles.append(classes.missile([x_rocket, y_rocket], [int(.5 + v_missile*m.cos(angle)), int(.5 + v_missile*m.sin(angle))]))

        #DEATH STAR
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            angle = m.atan2( (pygame.mouse.get_pos()[1] - y_rocket) , (pygame.mouse.get_pos()[0] - x_rocket) )
#            if len(bombs) == 0: bombs.append(classes.bomb([x_rocket, y_rocket], [int(.5 + v_bomb*m.cos(angle)), int(.5 + v_bomb*m.sin(angle))]))

        #QUITTING THE GAME
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("Your score was ",int(score))
            done = True

        #RESETTING THE GAME
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            print("Your score was ",int(score))
            score = 0
            asteroids = []
            x_rocket = int(x_screen / 2)
            y_rocket = int(y_screen / 2)
            vx_rocket = 0
            vy_rocket = 0

    if int(int(t/1000) % dt) == 0 and ticked == False:
        ticked = True
        okay = False
        while not okay:
            x_asteroid = r.randrange(0,x_screen)
            y_asteroid = r.randrange(0,y_screen)
            if functions.distance( [x_asteroid, y_asteroid], [x_rocket, y_rocket] ) > asteroid_spawn_buffer: okay = True
        asteroids.append(classes.asteroid(r.randrange(25,100), [x_asteroid, y_asteroid], [r.randrange(-4,5),r.randrange(-4,5)]))
    if int(t/1000) % dt > .1 and ticked == True: ticked = False
            
    screen.fill((0,0,0))
    pygame.transform.scale(get_image("background.jpg"),(x_screen,y_screen))
    screen.blit(get_image("background.jpg"),(0,0))
    pygame.draw.circle(screen, (255,255,255), (x_rocket,y_rocket), size_rocket) #ROCKET

    #LOOP OVER THE ASTEROIDS
    for asteroid in asteroids:
        asteroid.set_pos( [asteroid.pos[0]+asteroid.vel[0], asteroid.pos[1]+asteroid.vel[1]] )
        pygame.draw.circle(screen, (100,100,100), (asteroid.pos[0],asteroid.pos[1]), asteroid.size)
        if asteroid.pos[0] > x_screen or asteroid.pos[0] < 0: asteroid.set_vel([-asteroid.vel[0], asteroid.vel[1]])
        if asteroid.pos[1] > y_screen or asteroid.pos[1] < 0: asteroid.set_vel([asteroid.vel[0], -asteroid.vel[1]])

        #CHECK IF ANY ASTEROIDS HIT THE ROCKET
        if functions.distance([x_rocket, y_rocket], asteroid.pos) < (size_rocket + asteroid.size):
            print("Your score was ",int(score))
            score = 0
            asteroids = []
            x_rocket = int(x_screen / 2)
            y_rocket = int(y_screen / 2)
            vx_rocket = 0
            vy_rocket = 0

    #LOOP OVER THE BOMB
    for bomb in bombs:
        bomb.set_pos( [bomb.pos[0] + bomb.vel[0], bomb.pos[1] + bomb.vel[1]] )
        pygame.draw.circle(screen, (255,255,150), (bomb.pos[0], bomb.pos[1]), size_bomb)
        if bomb.pos[0] > x_screen or bomb.pos[0] < 0: bomb.set_vel([-bomb.vel[0], bomb.vel[1]])
        if bomb.pos[1] > y_screen or bomb.pos[1] < 0: bomb.set_vel([bomb.vel[0], -bomb.vel[1]])

        #CHECK IF THE BOMB HIT ANY ASTEROIDS
        for asteroid in asteroids:
            if functions.distance(asteroid.pos, bomb.pos) < asteroid.size + size_bomb:
                asteroids.remove(asteroid)
                bombs.remove(bomb)

    #LOOP OVER THE MISSILES
    for missile in missiles:
        missile.set_pos( [missile.pos[0] + missile.vel[0], missile.pos[1] + missile.vel[1]] )
        pygame.draw.circle(screen, (255,255,150), (missile.pos[0], missile.pos[1]), size_missile)
        if missile.pos[0] > x_screen or missile.pos[0] < 0:
            missiles.remove(missile)
            continue
        if missile.pos[1] > y_screen or missile.pos[1] < 0: missiles.remove(missile)

        #CHECK IF ANY MISSILES HIT ANY ASTEROIDS
        for asteroid in asteroids:
            if functions.distance(asteroid.pos, missile.pos) < asteroid.size + size_missile:
                asteroid.set_size(asteroid.size - 3)
                if asteroid.size < 20: asteroids.remove(asteroid)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        vy_rocket -= F
        if abs(vy_rocket) > v_max: vy_rocket = -v_max
    if pressed[pygame.K_a]:
        vx_rocket -= F
        if abs(vx_rocket) > v_max: vx_rocket = -v_max
    if pressed[pygame.K_s]:
        vy_rocket += F
        if abs(vy_rocket) > v_max: vy_rocket = v_max
    if pressed[pygame.K_d]:
        vx_rocket += F
        if abs(vx_rocket) > v_max: vx_rocket = v_max

    if not (pressed[pygame.K_d] or pressed[pygame.K_a]): vx_rocket = vx_rocket * .95
    if not (pressed[pygame.K_s] or pressed[pygame.K_w]): vy_rocket = vy_rocket * .95

    x_rocket = int(x_rocket + c*vx_rocket + .5)
    y_rocket = int(y_rocket + c*vy_rocket + .5)
    
    if x_rocket > x_screen or x_rocket < 0:
        vx_rocket = 0#-vx_rocket
        if x_rocket > x_screen: x_rocket = x_screen
        else: x_rocket = 0
    if y_rocket > y_screen or y_rocket < 0:
        vy_rocket = 0#-vy_rocket
        if y_rocket > y_screen: y_rocket = y_screen
        else: y_rocket = 0

    score = score + len(asteroids)/float(10)
    pygame.display.flip()
    t += clock.tick(60)
