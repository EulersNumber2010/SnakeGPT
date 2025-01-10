from rich import print
import os
import random

board = [
    list("╭────────────────────╮"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("│                    │"),
    list("╰────────────────────╯")
]

global xhist
global yhist
global hx
global hy
global d
global foodx
global foody
global length
global eaten
global runs

def initsymbol():
    global apple
    global head
    apple = "@"
    head = "O"
    upsymb = "█"
    downsymb = "█"
    lefttsymb = "█"
    rightsymb = "█"
initsymbol()

def draw_board():
    for row in board:
        print("".join(row))
    print(runs)
            
def spawn_head():
    board[hy][hx] = f"{head}"

def spawn_apple():
    foodx = random.randint(1, 20)
    foody = random.randint(1, 20)
    board[foody][foodx] = f"{apple}"
    eaten = False

def detect_apple():
    if hx == foodx and hy == foody:
        length += 1
        eaten = True

def init():
    # position history
    xhist = []
    yhist = []
    # x coordinates begin at 1 and end at 20 (0 is a wall, 21 is a wall)
    hx = 10
    # y coordinates begin at 1 and end at 20 (0 is a wall, 21 is a wall)
    hy = 10
    # false means that the apple is still on the board that turn, true means that it has been eaten
    eaten = False
    # number of turns elapsed (for init)
    runs = 0
    spawn_apple()
init()

def cycle():
    dir = str(input("Which direction do you want to go? (WASD)\n"))

    try:
        if dir == "w":
            d = "w"
            head = f"{upsymb}"
            hy = (hy-1)
        elif dir == "s":
            d = "s"
            head = f"{downsymb}"
            hy = (hy+1)
        elif dir == "a":
            d = "a"
            head = f"{lefttsymb}"
            hx = (hx-1)
        elif dir == "d":
            d = "d"
            head = f"{rightsymb}"
            hx = (hx+1)
        elif dir == "":
            if d == "w":
                d = "w"
                hy = (hy-1)
            elif d == "s":
                d = "s"
                hy = (hy+1)
            elif d == "a":
                d = "a"
                hx = (hx-1)
            elif d == "d":
                d = "d"
                hx = (hx+1)
    except NameError:
        print("A direction (WASD) must be input on the first turn!\nPLEASE RESTART")
    finally:
        xhist.append(hx)
        yhist.append(hy)

    spawn_head()
    if eaten == True:
        spawn_apple()
    if runs != 0:
        detect_apple()
    runs += 1
    draw_board()

if __name__ == "__main__":
    draw_board()
    spawn_head()
    draw_board()
    print ('''\nWe reccomend the font "Kreative Square" for optimal display of the game.
It can be obtained from https://www.kreativekorp.com/software/fonts/ksquare/\n''')
    while hx in range(1,21) and hy in range(1,21):
        cycle()
    print("You Lost :(")