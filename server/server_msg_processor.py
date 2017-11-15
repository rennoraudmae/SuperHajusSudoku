from common.message_processor import MessageProcessor
import common.constants as C
import common.message_types as T
from common.object_factory import ObjectFactory
from common.custom_exceptions import LogicException
import os.path
from os import listdir
from os.path import isfile, join

'''
This is server side message processor, which processes only server specific messages and operations.
'''


class ServerMsgProcessor(object, MessageProcessor):
    def __init__(self, server, source):
        super(ServerMsgProcessor, self).__init__()
        self.server = server
        self.source = source

    def ping(self):
        return " ", T.RESP_OK

    def new_game(self):
        params = self._message.split(":")
        game_name = params[0]
        max_players = params[1]
        new_game_id = self.server.add_new_game(game_name, max_players)
        return new_game_id, T.RESP_OK

    def get_all_games(self):
        sudoku_games = self.server.get_all_games()
        game_ids = " "
        for game in sudoku_games:
            game_ids = game_ids + game.get_id() + ", "
        # Remove tracing comma
        game_ids = game_ids[:-1]

        if len(game_ids) == 0:
            game_ids = "(No games available yet)"

        return game_ids, T.RESP_OK

    def join_game(self):
        params = self._message.split(":")
        game_id = params[0]
        username = params[1]
        try:
            success = self.server.add_player(game_id, username, self.source)
            if success:
                return " ", T.RESP_OK
            else:
                return "No such game. Please provide correct ID.", T.RESP_ERR
        except LogicException as e:
            return e.message, T.RESP_ERR

    def leave_game(self):
        params = self._message.split(":")
        game_id = params[0]
        username = params[1]
        self.server.remove_player(game_id, username)
        return " ", T.RESP_OK
    
    def check_nr(self):
        params = self._message.split(":")
        try:
            nr = params[0]
            address = params[1]
            game_id = params[2]
            username = params[3]
        except IndexError as e:
            return e.message, T.RESP_ERR
        if self.server.check_nr(game_id, username, nr, address):
            return " ", T.RESP_OK
        return " ", T.RESP_NOK
        
    def player_list(self):
        game_id = self._message
        try:
            players = self.server.get_game_player_list(game_id)
            return ObjectFactory.players_to_json(players), T.RESP_OK
        except LogicException as e:
            return e.message, T.RESP_ERR

    def get_game_field(self):
        game_id = self._message
        game_field = self.server.get_game_field(game_id)

        return ObjectFactory.field_to_json(game_field), T.RESP_OK

    def __error(self, message):
        return message, T.RESP_ERR
