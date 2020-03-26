from math import floor
import threading
import time
import copy
from board import Board
from solver import SudokuSolver
import generate

W_H = 50
solveable = None
generated = False

def is_valid():
    #check if board is valid and color board
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
    print("valid", valid)

def check_if_finished():
    # check if board is full and color board
    global board
    finished = True
    for i in range(9):
        for j in range(9):
            if board.field[i][j] == 0:
                finished = False
    if finished:
        board.draw_field("green")

def key(event):
    global board
    try:
        board.number = int(event.char)
    except:
        print("It has to be a number!")

def assign(event):
    global board
    x = floor(event.x/W_H)
    y = floor(event.y/W_H)
    if board.starting_field[x][y] == 0:
        if not board.field[x][y] == 0:
            board.redraw()
        board.field[x][y] = board.number
        board.draw_field("grey64")
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

    #animate backtracking
    while solveable == None:
        board.redraw()
        board.draw_field("SlateBlue3")

        board.platform.update()
        time.sleep(0.01)

    if solveable == True:
        board.draw_field("green3")
    else:
        board.draw_field("red")

    board.platform.update()

def start_new_game(event=None):
    global board, solveable
    solveable = None
    board.number = 0
    board.starting_field = []
    board.draw()

def generate_thread():
    global board, generated
    generated = generate.generate_field(board)

def generate_new(event=None):
    global board, generated
    if board.starting_field == []:
        board.starting_field = []
        for i in range(9):
            board.starting_field.append([])
            for j in range(9):
                board.starting_field[i].append(0)
                
        t = threading.Thread(target=generate_thread)
        t.daemon = True
        t.start()

        while generated == False:
            board.redraw()
            board.draw_field("orange")

            board.platform.update()
            time.sleep(0.01)

        board.redraw()
        board.draw_field("black")
        board.platform.update()

def load_sudoku(event=None):
    global board
    if board.starting_field == []:
        field = generate.get_random_field()
        board.field = field
        board.starting_field = copy.deepcopy(field)
        board.draw_field("grey")

board = Board("Sudoku", W_H)
board.draw()
board.platform.bind("<Key>", key)
board.platform.bind("<Button-1>", assign)
board.platform.bind("<space>", start_new_game)
board.platform.bind("<Return>", solve)
board.platform.bind("l", load_sudoku)
board.platform.bind("g", generate_new)
board.platform.focus_set()
board.start()