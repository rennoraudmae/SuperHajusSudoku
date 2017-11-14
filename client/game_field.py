from Tkinter import *
import tkMessageBox
import common.constants as C
from client.tcp_client import TcpClient
from common.custom_exceptions import LogicException

"""
This is GUI for playing the game.
"""

class GameField(Frame):
    def __init__(self, master, controller, client, game_id):
        Frame.__init__(self, master=master)
        self.master = master
        self.controller = controller
        self.draw_field()
        self.draw_numbers()
        self.draw_player_list()
        self.draw_buttons()
        self.client = client
        self.game_id = game_id
        
    def draw_field(self):
        #draws sudoku field on the canvas
        #each cell is drawn as rectangle and after that larger rectangles
        #are drawn on top to highlight 3x3 box borders
        self.canvas = Canvas(self, width=C.FIELD_SIDE, height=C.FIELD_SIDE)
        self.canvas.grid(row=0, column=1)
        
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
    
    def draw_numbers(self):
        numbers = [['-',1,'-','-',2,'-','-',3,'-'],
                  ['-',9,'-','-','-',4,'-','-','-'],
                  ['-',7,'-','-',5,'-',1,'-','-'],
                  [2,'-',1,'-','-','-','-','-',9],
                  ['-','-','-','-',8,1,'-',5,'-'],
                  ['-','-','-','-','-','-','-','-',4],
                  [9,'-','-',5,'-','-','-','-',2],
                  ['-','-','-',6,'-','-','-','-',3],
                  [3,'-','-','-','-','-',7,'-','-']]
    
        for i in range(9):
            for j in range(9):
                number = numbers[j][i]
                if not isinstance(number,int):
                    continue
                x=C.PADDING + i * C.CELL_SIDE + 0.5 * C.CELL_SIDE
                y=C.PADDING + j * C.CELL_SIDE + 0.5 * C.CELL_SIDE
                
                self.canvas.create_text(x, y, text=str(number), font=('Arial', 24))
    def draw_player_list(self):
        #draws player list
        self.player_board = Text(self, height=30, width=20)
        self.player_board.grid(row=0, column=0, padx=10, pady=10, sticky='wens')
        #self.player_board.insert(END, 'Player_1\t\t10\n')
        #self.player_board.insert(END, 'Player_2\t\t6\n')
        self.player_board.config(state=DISABLED)

    def draw_buttons(self):
        create_new_game_button = Button(self)
        create_new_game_button["text"] = "Leave Game"
        create_new_game_button["command"] = self.leave_game
        create_new_game_button.grid(row=3, column=0)

    def leave_game(self):
        self.client.leave_game(self.game_id)
        
    

