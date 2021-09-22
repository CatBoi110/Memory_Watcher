# Welcome to Memory Watcher.py 
# Created by Jack Levin 9/18/21

# This program will run in the background unless closed by the user

# Imports
import psutil
from psutil import virtual_memory
import time
from time import sleep
import pygame
import keyboard
import linecache
import os 
from os import sys
from pathlib import Path


# Variables
mem_percent = linecache.getline("config.txt",1)
warning = False
path = Path(__file__).with_name("Memory_Warning.pyw")

# Main loop, checks for memory usage and opens Memory_Warning.pyw if memory exceds value stated in setup
run = True
while run == True:
    time.sleep(1)

    # Breaks loop if f12 is held
    if keyboard.is_pressed("f12"):
        run = False
        break
        

    # Reads Used memory and checks if it over the target memory 
    memory = psutil.virtual_memory()

    # converts memory value from bytes to megabytes, dividing my 1e+6 converts bytes to megabytes
    available_memory = round(memory.available / 1e+6)
    total_memory = round(memory.total  / 1e+6)
    target_memory = round(total_memory * float(mem_percent))
    
    
    # Checks used memory to target memory 
    # If memory used is more than the target, it opens warning file and if memory used is less than the target is closes the file 
    if total_memory - available_memory >= target_memory:
        exec(open(path).read(),globals())

    if total_memory - available_memory < target_memory:
        pygame.display.quit()



   


