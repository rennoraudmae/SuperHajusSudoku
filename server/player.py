
class Player():
    def __init__(self, username, source):
        self.__username = username
        self.__source = source
        self.__score = 0

    def get_source(self):
        return self.__source

    def get_username(self):
        return self.__username