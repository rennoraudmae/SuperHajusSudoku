import re


class SudokuGame():
    def __init__(self, game_name, max_players=2):
        self.game_name = game_name
        self.max_players = max_players
        self.__id = re.sub('[^A-Za-z0-9]+', '', self.game_name)

    def get_id(self):
        return self.__id
