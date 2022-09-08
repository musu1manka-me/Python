import random
import os
import time
import colorama

for b in range(1,100):
    lst = [colorama.Fore.RED,colorama.Fore.BLUE,colorama.Fore.YELLOW,colorama.Fore.GREEN,colorama.Fore.CYAN]
    x = 100
    v = 200
    for v in range(1,x+1):
        prob = " "*(x-v)
        star = "I love my self <3 "*v
        print(random.choice(lst) + prob + star)
    time.sleep(0.07)  
    # os.system("cls")
    
