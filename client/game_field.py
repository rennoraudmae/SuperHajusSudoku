from Tkinter import *
import tkMessageBox
import common.constants as C
from client.tcp_client import TcpClient
from common.custom_exceptions import LogicException

"""
This is GUI for playing the game.
"""

class GameField(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master=master)
        self.pack(side="top", fill="both", expand=True)
        self.draw_field()
        
        
    def draw_field(self):
        self.canvas = Canvas(self, width=C.FIELD_SIDE, height=C.FIELD_SIDE)
        self.canvas.pack(fill="both", side="top")
        
        for i in range(9):
            for j in range(9):
                x0 = C.PADDING + i * C.CELL_SIDE
                y0 = C.PADDING + j * C.CELL_SIDE
                x1 = x0 + C.CELL_SIDE
                y1 = y0 + C.CELL_SIDE
                self.canvas.create_rectangle(x0, y0, x1, y1)
        for i in range(3):
            for j in range(3):
                x0 = C.PADDING + i*3 * C.CELL_SIDE
                y0 = C.PADDING + j*3 * C.CELL_SIDE
                x1 = x0 + 3 * C.CELL_SIDE
                y1 = y0 + 3 * C.CELL_SIDE
                self.canvas.create_rectangle(x0, y0, x1, y1, width=3)
                
                
    def draw_field_old(self):
        #code is based on the example found in the link:
        #http://newcoder.io/gui/part-3/
        self.canvas = Canvas(self, width=C.FIELD_SIDE, height=C.FIELD_SIDE)
        self.canvas.pack(fill="both", side="top")
        
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"
            x0 = C.PADDING + i * C.CELL_SIDE
            y0 = C.PADDING
            x1 = C.PADDING + i * C.CELL_SIDE
            y1 = C.FIELD_SIDE - C.PADDING
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=2)

            x0 = C.PADDING
            y0 = C.PADDING + i * C.CELL_SIDE
            x1 = C.FIELD_SIDE - C.PADDING
            y1 = C.PADDING + i * C.CELL_SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=2)