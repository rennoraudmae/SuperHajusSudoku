REQ_SIMPLE_MESSAGE = '1'
REQ_NEW_GAME = '2'
REQ_ALL_GAMES = '3'
REQ_JOIN_GAME = '4'
REQ_LEAVE_GAME = '5'
REQ_GAME_FIELD = '6'
REQ_PLAYER_LIST = '7'

RESP_OK = 'a'
RESP_VOID = 'b'
RESP_ERR = 'c'

'''
Here are defined all message types that can be sent and/or received with their functions.
The functions are implemented in corresponding msg_processor classes.
'''
MSG_TYPES = {REQ_SIMPLE_MESSAGE: 'simple_message',
             REQ_NEW_GAME: 'new_game',
             REQ_ALL_GAMES: 'get_all_games',
             REQ_JOIN_GAME: 'join_game',
             REQ_PLAYER_LIST: 'player_list',
             REQ_GAME_FIELD: 'game_field',
             REQ_LEAVE_GAME: 'leave_game',
             #
             RESP_OK: 'success',
             RESP_VOID: 'void',
             RESP_ERR: 'error'
             }
