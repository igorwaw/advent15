#!/usr/bin/python3


import pygame


# constants
INPUTFILE="18-input.txt"
WIDTH=100
HEIGHT=100
LIGHTSIZE=8 # on the screen each light will be 8x8 pixels
FPS=5 # how many animation frames / calculation steps per second
ROUNDS=100

VARIANT=False # set to False for Part1, True for Part2

cwhite=(255,255,255)
cblack=(0,0,0)

# global variables
lights1=[]
lights2=[]


########## FUNCTIONS - VISUALIZATION ##########

def print_lights(lights): # for debug
    for y in range(len(lights)):
        for x in range(len(lights[0])):
            try:
                if lights[y][x]:
                    print("#",end="")
                else:
                    print(".",end="")
            except IndexError:
                print("index error: ",x,y)
        print()

def write_below(message):
    global font, screen
    """ prints a message at the bottom of the window """
    text = font.render(message, True, (200,200,200), (0,0,0))
    textRect = text.get_rect()
    textRect.center = ((WIDTH*LIGHTSIZE) // 2, (HEIGHT*LIGHTSIZE)+20)
    screen.blit(text, textRect)

def redraw_screen(lights):
    global screen
    screen.fill(cblack) # Fill the background with black
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if lights[y][x]:
                #print(f"{x}x{y} ", end="")
                pygame.draw.rect(screen, cwhite, pygame.Rect(x*LIGHTSIZE,y*LIGHTSIZE,LIGHTSIZE,LIGHTSIZE))

########## FUNCTIONS - OTHER  ###########

def corners_on(lights):
    lights[0][0], lights[HEIGHT-1][0], lights[0][WIDTH-1], lights[HEIGHT-1][WIDTH-1] = True, True, True, True

def update_lights(source, target):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            num_neighbours=get_neighbours(source, x, y)
            if source[y][x]:
                if num_neighbours==2 or num_neighbours==3:
                    target[y][x]=True
                else:
                    target[y][x]=False
            else:
                if num_neighbours==3:
                    target[y][x]=True
                else:
                    target[y][x]=False
    if VARIANT:
        corners_on(target)
        

def get_neighbours(lights, x, y):
    num_neighbours=0
    for deltax in (-1, 0, 1):
        for deltay in (-1, 0, 1):
            if deltax==0 and deltay==0: 
                continue
            if (x+deltax<0) or (x+deltax>=WIDTH):
                continue
            if (y+deltay<0) or (y+deltay>=WIDTH):
                continue
            if lights[y+deltay][x+deltax]:
                #print("neighbour on: ", x+deltax, y+deltay)
                num_neighbours+=1
    return num_neighbours

########## INITIALIZATION  ###########

# read input
with open(INPUTFILE) as inputfile:
    for line in inputfile:
        lights1.append( [ x=='#' for x in line.strip() ] ) # saves True for every # or False otherwise
        lights2.append( [ x=='#' for x in line.strip() ] ) 
if VARIANT:
        corners_on(lights1)
        corners_on(lights2)
#print_lights(lights1)

# initialize pygame
pygame.init()
screen=pygame.display.set_mode((WIDTH*LIGHTSIZE, HEIGHT*LIGHTSIZE+40)) # extra height for text message
pygame.display.set_caption('Day 18: Like a GIF For Your Yard')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 20)
running=True
done=False

##########  MAIN LOOP   ###########
while running:
    if not done:
        for i in range(ROUNDS):
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running=False
            if not running: break             
            if (i%2==0):
                source, target = lights1, lights2
            else:
                source, target = lights2, lights1
            update_lights(source, target)
            redraw_screen(target)
            lit=sum(map(sum, target))
            write_below(f"Round: {i+1}, lights on: {lit}")
            pygame.display.flip()
            clock.tick(FPS) # delay here
        done=True # don't start iterating again, just wait for quit event
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running=False
        clock.tick(FPS) # or here

##########  ENDGAME  ###########

pygame.quit()
print ("Lights on: ", lit)
#print_lights(target)
