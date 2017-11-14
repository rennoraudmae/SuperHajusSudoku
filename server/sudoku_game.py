import re
import random


class SudokuGame():
    def __init__(self, game_name, max_players=2):
        self.game_name = game_name
        self.max_players = max_players
        self.__id = re.sub('[^A-Za-z0-9]+', '', self.game_name)
        self.players = []
        self.game_field, self.solution = self.__generate_puzzle()
        
    def get_id(self):
        return self.__id
    
    def __generate_puzzle(self):
        sudoku = [['-',1,'-','-',2,'-','-',3,'-'],
                  ['-',9,'-','-','-',4,'-','-','-'],
                  ['-',7,'-','-',5,'-',1,'-','-'],
                  [2,'-',1,'-','-','-','-','-',9],
                  ['-','-','-','-',8,1,'-',5,'-'],
                  ['-','-','-','-','-','-','-','-',4],
                  [9,'-','-',5,'-','-','-','-',2],
                  ['-','-','-',6,'-','-','-','-',3],
                  [3,'-','-','-','-','-',7,'-','-']]
        solution =[[5,1,4,8,2,6,9,3,7],
                   [8,9,3,1,7,4,6,2,5],
                   [6,7,2,3,5,9,1,4,8],
                   [2,8,1,4,6,5,3,7,9],
                   [4,3,9,7,8,1,2,5,6],
                   [7,5,6,9,3,2,8,1,4],
                   [9,6,7,5,1,3,4,8,2],
                   [1,2,8,6,4,7,5,9,3],
                   [3,4,5,2,9,8,7,6,1]] 
        return (sudoku, solution)
        
    def check_nr(self, nr, address):
        pass
    def add_nr(self, nr, address):
        pass
    def check_game_state(self):
        pass

    def add_player(self,username):
        self.players.append(username)

    def remove_player(self, username):
        self.players.remove(username)
