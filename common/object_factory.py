import json

'''
This class is for serializing and deserializing different objects for data trasfer between client and server
'''
class ObjectFactory():
    def __init__(self):
        pass

    @staticmethod
    def field_to_json(field):
        field_json = json.dumps(field)
        return field_json

    @staticmethod
    def field_from_json(field_json):
        field_arr = json.loads(field_json)
        return field_arr

    def players_to_json(players):
        players_json = json.dumps(players)
        return players_json

    def players_from_json(players_json):
        players = json.loads(players_json)
        return players