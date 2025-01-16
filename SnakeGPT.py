from rich import print
import os
import random

boardmaster = [
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

board = boardmaster

d = ""
foodx = 0
foody = 0
apple = "@"
head = "O"
body = "█"
length = 1

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


def spawn_apple():
    global foodx
    global foody
    global board
    global eaten
    foodx = random.randint(1, 20)
    foody = random.randint(1, 20)
    board[foody][foodx] = f"{apple}"
    eaten = False

def draw_board():
    global board
    board = boardmaster
    for i in range(0, len(xhist)-1):
        board[yhist[i]][xhist[i]] = body
    for row in board:
        print("".join(row))
    print(f"Turns: {runs} Length: {length}\nFood X: {foodx} Food Y: {foody}")
            

def spawn_head():
    global board
    board[hy][hx] = f"{head}"

def detect_apple():
    global length
    global eaten
    if hx == foodx and hy == foody:
        length += 1
        eaten = True

def cycle():
    dir = str(input("Which direction do you want to go? (WASD)\n"))

    global hx
    global hy
    global d
    global runs

    try:
        if dir == "w":
            d = "w"
            head = f"{body}"
            hy = (hy-1)
        elif dir == "s":
            d = "s"
            head = f"{body}"
            hy = (hy+1)
        elif dir == "a":
            d = "a"
            head = f"{body}"
            hx = (hx-1)
        elif dir == "d":
            d = "d"
            head = f"{body}"
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
    
    while len(xhist) > length:
        xhist.pop(0)    ### MATT: I THINK YOU MEAN: xhist.pop(0)  yhist.pop(0)
        yhist.pop(0)
    
    xhist.append(hx)
    yhist.append(hy)

    spawn_head()
    if eaten == True or runs == 0:
        spawn_apple()
    if runs != 0:
        detect_apple()
    runs += 1
    draw_board()

if __name__ == "__main__":
    draw_board()
    print ('''\nWe recommend the font "Kreative Square" for optimal display of the game.
It can be obtained from https://www.kreativekorp.com/software/fonts/ksquare/\n''')
    while hx in range(1,21) and hy in range(1,21):
        cycle()
    print("You Lost :(")