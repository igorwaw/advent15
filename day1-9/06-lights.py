#!/usr/bin/python3

import re
import pygame


# constants
INPUTFILE="06-input.txt"
WIDTH=1000
HEIGHT=1000
FPS=25 # how many animation frames / calculation steps per second

cwhite=(255,255,255)
cblack=(0,0,0)

# global variables
lights=[]



############ PARSE FILE

def run_cmd(cmd):
    elems=re.split(r'\s|,', cmd)
    if elems[0]=='toggle': rect_toggle( int(elems[1]), int(elems[2]), int(elems[4]), int(elems[5]) )
    elif elems[1]=='on'  : rect_on    ( int(elems[2]), int(elems[3]), int(elems[5]), int(elems[6]) )
    elif elems[1]=='off' : rect_off   ( int(elems[2]), int(elems[3]), int(elems[5]), int(elems[6]) )
    else: raise(ValueError)

e

########## FUNCTIONS ################

def rect_on(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights[i][j]=1
    pygame.draw.rect(screen, cwhite, pygame.Rect(x1,y1,x2-x1,y2-y1))
    

def rect_off(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights[i][j]=0
    pygame.draw.rect(screen, cblack, pygame.Rect(x1,y1,x2-x1,y2-y1))

def pixel_toggle(x,y):
    if lights[x][y]:
        lights[x][y]=0
        screen.set_at((x,y), cblack)
    else:
        lights[x][y]=1
        screen.set_at((x,y), cwhite)

def rect_toggle(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            pixel_toggle(i,j)


# initialize pygame
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Day 6: Probably a Fire Hazard')
clock = pygame.time.Clock()
screen.fill((0, 0, 0)) # Fill the background with black
running=True



# initialize the rest
lights = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
with open(INPUTFILE) as inputfile:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running=False

        if (line := inputfile.readline().rstrip()):
            run_cmd(line)
        pygame.display.flip()
        clock.tick(FPS) # wait here


    #end event loop, cleanup here
    pygame.quit()
    lit=sum(map(sum,lights))
    print(f"Lights on: {lit}, off: {WIDTH*HEIGHT-lit}")
