import tkinter as tk
from math import floor

class Board:
    '''Creates GUI Board'''

    def __init__(self, title, width):
        self.window = tk.Tk()
        self.window.title(title)
        self.width = width
        self.field = []
        self.number = 0
        self.platform = tk.Canvas(self.window, width = 9*width, height = 9*width)
        self.platform.pack()
        self.platform.bind("<Key>", self.key)
        self.platform.bind("<Button-1>", self.assign)
        self.platform.bind("<space>", self.start_new_game)
        self.platform.focus_set()

    def draw(self):
        self.field = []
        for i in range(9):
            self.field.append([])
            for j in range(9):
                self.field[i].append(0)
                self.platform.create_rectangle(i*self.width, j*self.width, (i+1)*self.width, (j+1)*self.width, fill="white")
        for i in [0, 3, 6]:
            self.platform.create_line(0, i*self.width, 9*self.width, i*self.width, width=3)
            self.platform.create_line(i*self.width, 0,  i*self.width, 9*self.width, width=3)

    def redraw(self):
        for i in range(9):
            for j in range(9):
                self.platform.create_rectangle(i*self.width, j*self.width, (i+1)*self.width, (j+1)*self.width, fill="white")
        for i in [0, 3, 6]:
            self.platform.create_line(0, i*self.width, 9*self.width, i*self.width, width=3)
            self.platform.create_line(i*self.width, 0,  i*self.width, 9*self.width, width=3)

    def draw_field(self, color):
        rndfont = 25
        for i in range(9):
            for j in range(9):
                if not (self.field[i][j] == 0):
                    self.platform.create_text((self.width/2)*((i*2)+1), (self.width/2)*((j*2)+1), text=self.field[i][j], font=('Pursia', rndfont), anchor="center", fill=color, tag=self.field[i][j])

    def color(self, coordinate_list, color):
        rndfont = 25
        for i, j in coordinate_list:
            if not self.field[i][j] == 0:
                self.platform.create_text((self.width/2)*((i*2)+1), (self.width/2)*((j*2)+1), text=self.field[i][j], font=('Pursia', rndfont), anchor="center", fill=color, tag=self.field[i][j])

    def start(self):
        self.window.mainloop()

    def key(self, event):
        #print(repr(event.char))
        try:
            self.number = int(event.char)
        except:
            print("It has to be a number!") 

    def assign(self, event):
        if not self.number == 0:
            x = floor(event.x/W_H)
            y = floor(event.y/W_H)
            if not self.field[x][y] == 0:
                self.redraw()
            self.field[x][y] = self.number
            self.draw_field("black")
            self.number = 0

    def start_new_game(self, event=None):
        self.number = 0
        self.draw()

W_H = 50
board = Board("Sudoku", W_H)
board.draw()
board.start()