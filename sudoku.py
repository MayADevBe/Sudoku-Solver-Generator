from math import floor
from board import Board

W_H = 50

def is_valid():
    global board
    valid = True
    
    for i in range(9):
        #check rows
        row = board.field[i]
        row = list(filter(lambda a: a != 0, row)) # 0 is empty cell
        if not len(row) == len(set(row)):
            #TODO invalid red
            valid = False

        #check columns
        column = [row[i] for row in board.field]
        column = list(filter(lambda a: a != 0, column))
        if not len(column) == len(set(column)):
            #TODO invalid red
            valid = False

    #check squares
    for row in [0, 3, 6]:
        for column in [0, 3, 6]:
            square = []
            for r in range(row, row+3):
                for c in range(column, column+3):
                    if not board.field[r][c] == 0:
                        square.append(board.field[r][c])
            if not len(square) == len(set(square)):
                #TODO invalid red
                valid = False
    
    if valid:
        check_if_finished()

def check_if_finished():
    global board
    finished = True
    for i in range(9):
        for j in range(9):
            if board.field[i][j] == 0:
                finished = False
    board.draw_field("green")

def key(event):
    #print(repr(event.char))
    try:
        self.number = int(event.char)
    except:
        print("It has to be a number!") 

def assign(event):
    if not board.number == 0:
        x = floor(event.x/W_H)
        y = floor(event.y/W_H)
        if not board.field[x][y] == 0:
            board.redraw()
        board.field[x][y] = board.number
        board.draw_field("black")
        board.number = 0
        is_valid()

def start_new_game(event=None):
    board.number = 0
    board.draw()

board = Board("Sudoku", W_H)
board.draw()
board.platform.bind("<Key>", key)
board.platform.bind("<Button-1>", assign)
board.platform.bind("<space>", start_new_game)
board.platform.focus_set()
board.start()