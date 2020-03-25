import copy
from board import Board
import time

class SudokuSolver:

    def __init__(self, board):
       self.board = board

    def check_if_finished(self):
        for i in range(9):
            for j in range(9):
                if self.board.field[i][j] == 0:
                    return False
        return True

    

    #A function to check if the grid is full
    def checkGrid(self, grid):
        for row in range(0,9):
            for col in range(0,9):
                if grid[row][col]==0:
                    return False

        #We have a complete grid!  
        return True 

    #A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def solve_soduku(self):
        #Find next empty cell
        for i in range(0,81):
            row=i//9
            col=i%9
            if self.board.field[row][col]==0:
                for value in range (1,10):
                    #Check that this value has not already be used on this row
                    if not(value in self.board.field[row]):
                    #Check that this value has not already be used on this column
                        if not value in [rows[col] for rows in self.board.field]:
                            #Identify which of the 9 squarsoes we are working on
                            square=[]
                            if row < 3:
                                r = 0
                            elif row < 6:
                                r = 3
                            else:
                                r = 6
                            if col < 3:
                                c = 0
                            elif col < 6:
                                c = 3
                            else:
                                c = 6
                            square = [self.board.field[i][c:(c+3)] for i in range(r, (r+3))]
                            #Check that this value has not already be used on this 3x3 square
                            if not value in [rows for rows in square]:
                                self.board.field[row][col]=value
                                time.sleep(0.01)       
                                if self.check_if_finished():
                                    print("Grid Complete and Checked")
                                    return True
                                else:
                                    if self.solve_soduku():
                                        return True
                break
        #print("Backtrack")
        self.board.field[row][col]=0  
