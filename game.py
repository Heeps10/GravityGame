# Gravity game where goal is to evade gravity circles as they fly across the screen pulling you in
import pygame
from pygame.locals import *
import random
import math
from direction import direction, gravity

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1680, 1120))
clock = pygame.time.Clock()
running = True
dt = 0

#x/y of display
w, h = pygame.display.get_surface().get_size()

#player values
player_vel = 600
player_mass = 50

#Object Values
circ_x, circ_y = -200, random.randint(16, 1049)
circ_gravity = 20
circ_mass = 10000

#init player shape info
rect_color = "white"
rect = pygame.FRect(w/2, h/2, 50, 50)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #draws the rect and circle
    pygame.draw.rect(screen, rect_color, rect)

    #draws and moves circle
    circ = pygame.draw.circle(screen, "red", (circ_x, circ_y), 25)
    circ_x += 60 * dt

    #resets circle pos when it reaches end of screen
    if circ_x > 1700:
        circ_x = -200
        circ_y = random.randint(16, 1049)
    
    #dd[0] is the theta, dd[1] is the distance
    dd = direction(rect[0], rect[1], circ_x, circ_y)

    #finds accel and converts to change in distance, or movement
    accel = gravity(dd[1], player_mass, circ_mass, circ_gravity)
    movement = accel * dt * dt

    #Works, figure out what to do when its too close but doesn't collide, center rect location, new object?, look up grav tutorials to figure out better solution to distance problem.
    #Make into function or do oop to make this easier to add onto new objects
    #checks direction to determine where movement should be given
    if dd[0] >= 0 and dd[0] <= 90:
        rect[0] -= abs(movement * math.cos(dd[0]))
        rect[1] += abs(movement * math.sin(dd[0]))
        #print(movement * math.sin(dd[0]))
    if dd[0] > 90 and dd[0] <= 180:
        rect[0] += abs(movement * math.cos(dd[0]))
        rect[1] += abs(movement * math.sin(dd[0]))
        #print("Q2")
    if dd[0] < 0 and dd[0] >= -90:
        rect[0] -= abs(movement * math.cos(dd[0]))
        rect[1] -= abs(movement * math.sin(dd[0]))
        #print("Q3")
    #works
    if dd[0] < -90 and dd[0] >= -180:
        rect[0] += movement * math.cos(dd[0])
        rect[1] -= movement * math.sin(dd[0])
        #print("Q4")

    #gets keys pressed and moves rect based on the seconds since last frame
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect[1] -= player_vel * dt
        #print(player_vel * dt)
        #print(rect[1])
    if keys[pygame.K_s]:
        rect[1] += player_vel * dt
        #print(rect[1])
    if keys[pygame.K_a]:
        rect[0] -= player_vel * dt
        #print(rect[0])
    if keys[pygame.K_d]:
        rect[0] += player_vel * dt
        #print(rect[0])
    #print("x ", rect[0])
    #print("y ", rect[1])

    #use for gravity
    dd = direction(rect[0], rect[1], circ_x, circ_y)
    #print("Direction : ", dd[0], "Distance: ", dd[1])

    #circ is multiple rects making this collision check possible
    if pygame.FRect.colliderect(rect, circ):
        rect_color = "green"
        print("Collision!")
    else:
        rect_color = "white"

    # flip() the display to put work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    
pygame.quit()
