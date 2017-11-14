import ntpath
import common.constants as C
from common.custom_exceptions import CommunicationException, LogicException
from common.message_publisher import MessagePublisher
from common.message_receiver import MessageReceiver
from client.client_msg_processor import ClientMsgProcessor
import common.message_types as T
from socket import socket, AF_INET, SOCK_STREAM
from socket import error as soc_error, timeout
import sys

'''
This is main class for TCP client. It establishes a connection with server.
It also initializes sending different commands to server and receives responses from server.
'''


class TcpClient():
    def __init__(self, host=C.DEFAULT_SERVER_HOST, port=C.DEFAULT_SERVER_PORT):
        self.__host = host
        self.__port = port
        self.__connected = False

        try:
            self.__socket = socket(AF_INET, SOCK_STREAM)
            self.__socket.connect((self.__host, self.__port))
            self.__socket.settimeout(60)
            self.__connected = True
        except Exception as e:
            C.LOG.error('Can\'t connect to server, error : %s' % str(e))
            return

        self.__message_publisher = MessagePublisher(socket=self.__socket)
        self.__message_receiver = MessageReceiver(socket=self.__socket, processor=ClientMsgProcessor())

    def is_connected(self):
        return self.__connected

    def send_message(self, message):
        msg, type = self.__send_message(message, T.REQ_SIMPLE_MESSAGE)
        if type == T.RESP_OK:
            C.LOG.info("Got answer to simple message: {}".format(msg))
        else:
            C.LOG.warning(msg)

    def new_game_request(self, game_name, max_players):
        msg, type = self.__send_message("{}:{}".format(game_name, max_players), T.REQ_NEW_GAME)
        if type == T.RESP_OK:
            C.LOG.info("New game created with id: {}".format(msg))
            return msg
        else:
            C.LOG.warning(msg)
            raise LogicException("New game creation failed with message: {}".format(msg))

    def join_game(self, game_id, username):
        msg, type = self.__send_message("{}:{}".format(game_id, username), T.REQ_JOIN_GAME)
        if type == T.RESP_OK:
            C.LOG.info("Joined game with id: {}".format(game_id))
        else:
            C.LOG.warning(msg)
            raise LogicException("New game creation failed with message: {}".format(msg))

    def leave_game(self, game_id):
        msg, type = self.__send_message(game_id, T.REQ_LEAVE_GAME)
        if type == T.RESP_OK:
            C.LOG.info("Left game with id: {}".format(game_id))
        else:
            C.LOG.warning(msg)
            raise LogicException("Leaving game failed with: {}".format(msg))


    def get_all_games(self):
        msg, type = self.__send_message(" ", T.REQ_ALL_GAMES)
        if type == T.RESP_OK:
            return msg
        else:
            C.LOG.warning(msg)
            raise LogicException("Game requesting failed with error: {}".format(msg))
    
    def get_player_list(self):
        pass
        
    def get_game_field(self):
        pass
        
    def send_new_nr(self):
        pass

    def __send_message(self, message, type):
        if not self.__connected:
            raise CommunicationException("Server not connected")

        if len(type) > 0:
            try:
                self.__message_publisher.publish(message_and_type=(message, type))
                return self.__message_receiver.receive()
            except soc_error as e:
                C.LOG.error('Couldn\'t get response from server, error : %s' % str(e))
            except Exception as e:
                C.LOG.error("Exception on processing response: {}".format(e))
