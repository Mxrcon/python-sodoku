
import random

square = [[1,2,3],[4,5,6],[7,8,9]]
def get_square():
    line =[i for i in range(1,10)]
    lst = random.sample(line, 9)
    square =  [lst[i:i + 3] for i in range(0, len(lst), 3)]
    return square


def valid_line(line):
    if sorted(line) == [1,2,3,4,5,6,7,8,9]: return True
    else: return False
def get_3_lines():
    square_list= [get_square(),get_square(),get_square()]
    lines = []
    for i in range(0,3):
        lines.append(
       square_list[0][i]+square_list[1][i]+square_list[2][i])
    return lines
def get_board():
    board = get_3_lines()+get_3_lines()+get_3_lines()
    return board

def all_valid_lines(board):
    for i in board:
        if valid_line(i) == False:
            return False
    return True
def all_valid_columms(board):
    transposed_Board= [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    return all_valid_lines(transposed_Board)

x = 0
counter=0
while x == 0:
    counter+=1
    b = get_board()
    if all_valid_lines(b) and all_valid_columms(b) == True:
        print(b)
        print(counter)
        x=1

print("ok")
