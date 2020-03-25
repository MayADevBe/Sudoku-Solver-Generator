import tkinter as tk

class Board:
    '''Creates GUI Board'''

    def __init__(self, title, width):
        self.window = tk.Tk()
        self.window.title(title)
        self.width = width
        self.field = []
        self.starting_field = []
        self.number = 0
        self.platform = tk.Canvas(self.window, width = 9*width, height = 9*width)
        self.platform.pack()

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
                if not (self.starting_field[i][j] == 0):
                    self.platform.create_text((self.width/2)*((i*2)+1), (self.width/2)*((j*2)+1), text=self.starting_field[i][j], font=('Pursia', rndfont), anchor="center", fill="black", tag=self.starting_field)
                elif not (self.field[i][j] == 0):
                    self.platform.create_text((self.width/2)*((i*2)+1), (self.width/2)*((j*2)+1), text=self.field[i][j], font=('Pursia', rndfont), anchor="center", fill=color, tag=self.field[i][j])             

    def color(self, coordinate_list, color):
        rndfont = 25
        for i, j in coordinate_list:
            if not self.field[i][j] == 0:
                self.platform.create_text((self.width/2)*((i*2)+1), (self.width/2)*((j*2)+1), text=self.field[i][j], font=('Pursia', rndfont), anchor="center", fill=color, tag=self.field[i][j])

    def start(self):
        self.window.mainloop()