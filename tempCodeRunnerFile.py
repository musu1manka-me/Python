import random
import os
import time
import colorama

for b in range(1,100):
    lst = [colorama.Fore.RED,colorama.Fore.BLUE,colorama.Fore.YELLOW,colorama.Fore.GREEN,colorama.Fore.CYAN]
    x = 40
    for v in range(1,x+1):
        prob = " "*(x-v)
        star = "* "*v
        print(random.choice(lst) + prob + star)
    time.sleep(0.06)  
    os.system("cls")
    
