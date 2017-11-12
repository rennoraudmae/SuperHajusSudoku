from common.message_processor import MessageProcessor
import common.constants as C
import common.message_types as T
import os.path
from os import listdir
from os.path import isfile, join

'''
This is server side message processor, which processes only server specific messages and operations.
'''


class ServerMsgProcessor(object, MessageProcessor):
    def __init__(self, server):
        super(ServerMsgProcessor, self).__init__()
        self.server = server

    def ping(self):
        return "", T.RESP_OK

    def new_game(self):
        params = self._message.split(":")
        game_name = params[0]
        max_players = params[1]
        self.server.add_new_game(game_name, max_players)
        return self.success()

    def get_all_games(self):
        sudoku_games = self.server.get_all_games()
        game_names = ""
        for game in sudoku_games:
            game_names = game_names + game.game_name + ","
        # Remove tracing comma
        game_names = game_names[:-1]

        if len(game_names) == 0:
            game_names="(No games available yet)"

        return game_names, T.RESP_OK

    def __error(self, message):
        return message, T.RESP_ERR
