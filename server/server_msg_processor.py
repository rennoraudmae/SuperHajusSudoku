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
        new_game_id = self.server.add_new_game(game_name, max_players)
        return new_game_id, T.RESP_OK

    def get_all_games(self):
        sudoku_games = self.server.get_all_games()
        game_ids = ""
        for game in sudoku_games:
            game_ids = game_ids + game.get_id() + ", "
        # Remove tracing comma
        game_ids = game_ids[:-1]

        if len(game_ids) == 0:
            game_ids = "(No games available yet)"

        return game_ids, T.RESP_OK

    def join_game(self):
        game_id = self._message
        return " ", T.RESP_OK

    def leave_game(self):
        game_id = self._message
        return " ", T.RESP_OK

    def get_player_list(self):
        pass

    def get_game_field(self):
        pass

    def __error(self, message):
        return message, T.RESP_ERR
