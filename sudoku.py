from math import floor
import threading
import time
from board import Board
from solver import SudokuSolver

W_H = 50
solveable = None

def is_valid():
    global board
    valid = True
    coordinates = []
    for i in range(9):
        #check rows
        row = board.field[i]
        row = list(filter(lambda a: a != 0, row)) # 0 is empty cell
        if not len(row) == len(set(row)):
            for j in range(9):
                coordinates.append((i, j))
            valid = False

        #check columns
        column = [row[i] for row in board.field]
        column = list(filter(lambda a: a != 0, column))
        if not len(column) == len(set(column)):
            for j in range(9):
                coordinates.append((j, i))
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
                for r in range(row, row+3):
                    for c in range(column, column+3):
                        coordinates.append((r, c))
                valid = False
    
    if not valid:
        board.color(coordinates, 'red')
    else:
        check_if_finished()

def check_if_finished():
    global board
    finished = True
    for i in range(9):
        for j in range(9):
            if board.field[i][j] == 0:
                finished = False
    if finished:
        board.draw_field("green")

def key(event):
    #print(repr(event.char))
    try:
        board.number = int(event.char)
    except:
        print("It has to be a number!")

def assign(event):
    x = floor(event.x/W_H)
    y = floor(event.y/W_H)
    if not board.field[x][y] == 0:
        board.redraw()
    board.field[x][y] = board.number
    board.draw_field("black")
    board.number = 0
    is_valid()

def solver_thread():
    global solveable, solver
    solveable = solver.solve_soduku()

def solve(event=None):
    global board, solver
    solver = SudokuSolver(board)
    
    t = threading.Thread(target=solver_thread)
    t.daemon = True
    t.start()

    while solveable == None:
        board.redraw()
        board.draw_field("black")

        board.platform.update()
        time.sleep(0.01)

    if solveable == True:
        board.draw_field("green")
    else:
        board.draw_field("red")

    board.platform.update()

def start_new_game(event=None):
    board.number = 0
    board.draw()

board = Board("Sudoku", W_H)
board.draw()
field = [[3, 0, 6, 5, 0, 8, 4, 0, 0], [5, 2, 0, 0, 0, 0, 0, 0, 0], [0, 8, 7, 0, 0, 0, 0, 3, 1], [0, 0, 3, 0, 1, 0, 0, 8, 0], [9, 0, 0, 8, 6, 3, 0, 0, 5], [0, 5, 0, 0, 9, 0, 6, 0, 0], [1, 3, 0, 0, 0, 0, 2, 5, 0], [0, 0, 0, 0, 0, 0, 0, 7, 4], [0, 0, 5, 2, 0, 6, 3, 0, 0]]
board.field = field
board.draw_field("black")

board.platform.bind("<Key>", key)
board.platform.bind("<Button-1>", assign)
board.platform.bind("<space>", start_new_game)
board.platform.bind("<Return>", solve)
board.platform.focus_set()
board.start()