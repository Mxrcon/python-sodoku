import random
import time
#solver based on https://www.youtube.com/watch?v=G_UYXzGuqvM
#rulings of possible
def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] ==n :
                return False
        if grid[i][x] ==n :
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if grid[y0+i][x0+j]==n:
                    return False

    return True


#solver
solve_counter = 0
def solve():
    global solve_counter
    global grid

    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x]=n
                        solve()
                        if solve_counter >1:
                            return
                        grid[y][x] = 0
                return
    solve_counter+=1

def generator():
    global grid
    grid =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for i in range(10):
        x,y,n = random.randint(0, 8),random.randint(0, 8),random.randint(1, 9)
        if grid[y][x]==0:
            if possible(y,x,n):
                grid[y][x]=n
    solve()
    return grid
