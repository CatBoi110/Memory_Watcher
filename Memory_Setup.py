# Welcome to Memory_Setup.py :)
# Created by Jack Levin 9/17/21

# This program will act as a way to set the threshold for memory usage.

# Imports
import os
from os import sys
import linecache
import time
from time import sleep



# Function
def space():
    print("")


print("\\\ Welcome to Memory Watcher Setup Utility! //")
space()

press_enter = input("Press Enter to Begin! ")

space()

# Max amount of memory before warning appears (recomended: 80% - 90% of max system memory)
mem_percent = input("| What percentage of memory do you want to be used before the warning activates? | ** If unsure input 0.8 or 0.9 ** ")

# Checks if value is float, if not it closes the progam 
try:
    float(mem_percent)
except ValueError:
    print(" || Please a number equal to or less than one! ||")
    time.sleep(3)
    exit()

# Checks if value is > 1, it so it closes the program
if float(mem_percent) > 1:
    print(" || Please a number equal to or less than one! ||")
    time.sleep(3)
    exit()


# Opens config file where inputs are stored for later use (sys.path[0] is the same direcotry as the running python file)
with open(os.path.join(sys.path[0], "config.txt"), "r+") as f:
    write_total_mem = f.write(mem_percent)
   

print("|| Inputs has been saved! ||")

time.sleep(3)

f.closed