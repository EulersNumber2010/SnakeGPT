from rich import print
import os
head = "O"

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
global runs
xhist = []
yhist = []
runs = 0

# x coordinates begin at 1 and end at 20 (0 is a wall, 21 is a wall)
hx = 10
# y coordinates begin at 1 and end at 20 (0 is a wall, 21 is a wall)
hy = 10

def draw_board():
    for row in board:
        print("".join(row))
        if runs == 0:
            os.system("clear")
            
def spawn_head():
    board[hy][hx] = f"{head}"

def cycle():
    dir = str(input("Which direction do you want to go? (WASD)\n"))
    global hx
    global hy
    global d
    global head

    try:
        if dir == "w":
            d = "w"
            head = "⇧"
            hy = (hy-1)
        elif dir == "s":
            d = "s"
            head = "⇩"
            hy = (hy+1)
        elif dir == "a":
            d = "a"
            head = "⇦"
            hx = (hx-1)
        elif dir == "d":
            d = "d"
            head = "⇨"
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
        os.system("clear")
        runs = runs + 1

    
    spawn_head()
    draw_board()

if __name__ == "__main__":
    draw_board()
    spawn_head()
    draw_board()
    while hx in range(1,21) and hy in range(1,21):
        cycle()
    print("You Lost :(")