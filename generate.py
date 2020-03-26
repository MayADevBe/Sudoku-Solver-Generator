import json
import os.path
import random
from copy import deepcopy
from solver import SudokuSolver
from board import Board

def save_field(field):
    #save sudoku in json file
    fields = load_fields()
    fields.append(field)
    with open("fields.json", 'w') as f:
        json.dump(fields, f)

def load_fields():
    #load sudoku fields
    try:
        with open("fields.json", "r") as f:
            fields = json.load(f)     
        return fields
    except:
        with open("fields.json", "w") as f:
            fields = []
            json.dump(fields, f)
    return fields

def get_random_field():
    #get random field from safed fields or generate field
    fields = load_fields()
    if len(fields) > 0:
        r = random.randint(0, len(fields)-1)
        return fields[r]
    else:
        board = Board("Generate Sudoku", 50)
        board.draw()
        return generate_field(board)

def generate_field(board):
    #generate fully solved field
    print("Generate Sudoku")
    solver = SudokuSolver(board)
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(values)
    solver.solve_soduku(values=values)
    print("Full Board - Now removing numbers")
    #remove numbers one by one
    attempts = 5 # higher number = potential higher difficulty
    solver.counter = 1
    while attempts > 0:
        #select random cell, that is not empty
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board.field[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        value = board.field[row][col] #backup value
        board.field[row][col] = 0

        copy_field = deepcopy(board.field) #TODO change? - understand what is goal
        solver.counter = 0
        solver.solve_soduku(generate=True, field=copy_field)
        if solver.counter != 1:
            board.field[row][col] = value
            attempts -= 1
            print("Attempt down")

    board.starting_field = deepcopy(board.field)
    save_field(board.starting_field)
    return True