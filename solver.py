import copy
from board import Board
import time

class SudokuSolver:

    def __init__(self, board):
       self.board = board
       self.counter = 0

    def check_if_finished(self, field):
        for i in range(9):
            for j in range(9):
                if field[i][j] == 0:
                    return False
        return True

    #A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def solve_soduku(self, generate=False, values=[1, 2, 3, 4, 5, 6, 7, 8, 9], field=None):
        if field==None:
            field = self.board.field
        #Find next empty cell
        for i in range(0,81):
            row=i//9
            col=i%9
            if field[row][col]==0:
                for value in values:
                    #Check that this value has not already be used on this row
                    if not(value in field[row]):
                    #Check that this value has not already be used on this column
                        if not value in [rows[col] for rows in field]:
                            #Identify which of the 9 squarsoes we are working on
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[field[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[field[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[field[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[field[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[field[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[field[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[field[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[field[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[field[i][6:9] for i in range(6,9)]
                            #Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                field[row][col]=value
                                if not generate:
                                    time.sleep(0.01)     
                                if self.check_if_finished(field):
                                    # for generate to check if unique solution
                                    if generate and self.counter <= 1:
                                        self.counter += 1
                                    else:
                                        #print("Field Solved")
                                        return True
                                    break
                                else:
                                    if self.solve_soduku(generate, values, field):
                                        return True
                break
        #print("Backtrack")
        field[row][col]=0  
