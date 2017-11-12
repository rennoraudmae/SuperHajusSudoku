import ntpath
import common.constants as C
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

        try:
            self.__socket = socket(AF_INET, SOCK_STREAM)
            self.__socket.connect((self.__host, self.__port))
            self.__socket.settimeout(60)
        except Exception as e:
            C.LOG.error('Can\'t connect to server, error : %s' % str(e))

        self.__message_publisher = MessagePublisher(socket=self.__socket)
        self.__message_receiver = MessageReceiver(socket=self.__socket, processor=ClientMsgProcessor())

    def send_message(self, message):
        msg, type = self.__send_message(message, T.REQ_SIMPLE_MESSAGE)
        if type == T.RESP_OK:
            C.LOG.info("Got answer to simple message: {}".format(msg))
        else:
            C.LOG.warning(msg)

    def __send_message(self, message, type):
        if len(message) > 0:
            try:
                self.__message_publisher.publish(message_and_type=(message, type))
                return self.__message_receiver.receive()
            except soc_error as e:
                C.LOG.error('Couldn\'t get response from server, error : %s' % str(e))
            except Exception as e:
                C.LOG.error("Exception on processing response: {}".format(e))
