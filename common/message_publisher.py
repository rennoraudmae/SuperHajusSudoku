import common.constants as C
import common.message_types as TYPES
from socket import SHUT_WR, SHUT_RD
from socket import socket, AF_INET, SOCK_STREAM
from socket import error as soc_err


class MessagePublisher():
    def __init__(self, socket, message_and_type):
        self.__message, self.__type = message_and_type
        if self.__type not in TYPES.MSG_TYPES:
            raise Exception("Wrong message type: {}".format(self.__type))

        self.__socket = socket
        self.__message = "{}{}{}{}".format(self.__type, C.DELI, self.__message, C.MESSAGE_TERMINATOR)

    def publish(self):
        self.__socket.send(self.__message)
