from Tkinter import *
import tkMessageBox
import common.constants as C
from client.tcp_client import TcpClient


class MultiplayerGame(Frame):
    def __init__(self, client, username, master, controller):
        Frame.__init__(self, master=master)
        self.controller = controller
        #
        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.client = client
        self.username = username
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass
