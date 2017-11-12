from Tkinter import *
import tkMessageBox
import common.constants as C
from client.tcp_client import TcpClient
from common.custom_exceptions import LogicException


class MultiplayerGame(Frame):
    def __init__(self, client, username, master, controller):
        Frame.__init__(self, master=master)
        self.controller = controller
        #
        self.game_name_input = None
        self.all_games_var = StringVar()
        self.all_games_var.set("")
        self.max_users_input = None
        #
        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.client = client
        self.username = username
        self.pack()
        self.create_widgets()
        #

    def create_widgets(self):
        #Row 0
        Label(self, text="Logged in user: {}".format(self.username)).grid(row=0, column=0)
        #Row 1
        Label(self, text="Available games:").grid(row=1, column=0)
        Label(self, textvariable=self.all_games_var).grid(row=1, column=1)
        get_games_button = Button(self)
        get_games_button["text"] = "Refresh games list",
        get_games_button["command"] = self.retreive_all_games
        get_games_button.grid(row=1, column=3)
        self.retreive_all_games()
        #Row 2
        Label(self, text="Create new game").grid(row=2, column=0)
        self.game_name_input = Entry(self)
        self.game_name_input.insert(0, "(insert game name)")
        self.game_name_input.grid(row=2, column=1)
        self.max_users_input = Entry(self)
        self.max_users_input.insert(0, "(insert max players number)")
        self.max_users_input.grid(row=2, column=2)
        #Row 3
        create_new_game_button = Button(self)
        create_new_game_button["text"] = "Create new game",
        create_new_game_button["command"] = self.create_new_game
        create_new_game_button.grid(row=3, column=1)

    def retreive_all_games(self):
        self.all_games_var.set(self.client.get_all_games())

    def create_new_game(self):
        if len(self.game_name_input.get()) <= 0:
            tkMessageBox.showinfo("Message", "Please provide a game name")
            return

        try:
            max_players = int(self.max_users_input.get())
        except ValueError:
            tkMessageBox.showinfo("Message", "Please provide valid max players number")
            return

        try:
            self.client.new_game_request(self.game_name_input.get(), max_players)
            self.retreive_all_games()
        except LogicException as e:
            tkMessageBox.showerror("Error", e.message)
