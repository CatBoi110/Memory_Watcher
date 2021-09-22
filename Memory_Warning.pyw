# Welcome to Memory_Warning.pyw
# Created by Jack Levin 9/20/21


# This program only runs if Memory_Watcher.pyw is running and the amount of memory used is exceded by a certain threshold
# Imports
import pygame
import psutil
from psutil import virtual_memory
import time
from time import sleep
import pygame
import keyboard
import linecache
import os  

# Pygame variables
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
font_small = pygame.font.SysFont("None", 23)
font_meduim = pygame.font.SysFont("None", 35)
font_big = pygame.font.SysFont("None", 80)

# Gets value from config.txt
mem_percent = linecache.getline("config.txt",1)


# Pygame Window 
time.sleep(1)
win.fill((255, 255, 255))

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

# Gets available memory
memory = psutil.virtual_memory()
available_memory = round(memory.available / 1e+6)

# Prints Available Memory on line 2 
line_1 = font_big.render("Warning", True, (150, 0, 0))
line_2 = font_meduim.render("You only have " + str(available_memory) + " MB left of memory!", True, (0, 0, 0))
line_3 = font_small.render("To close this box either free up some memory or press the X button", True, (0, 0, 0))

# Displays text
win.blit(line_1, (140, 25))
win.blit(line_2, (25, 100))
win.blit(line_3, (12, 150))


pygame.display.update()
clock.tick(60)
