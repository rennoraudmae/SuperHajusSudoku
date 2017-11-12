import ntpath
import common.constants as C
from common.message_publisher import MessagePublisher
from common.message_receiver import MessageReceiver
from client.client_msg_processor import ClientMsgProcessor
import common.message_types as T
from socket import socket, AF_INET, SOCK_STREAM
from socket import error as soc_error, timeout
import sys


class TcpClient():
    def __init__(self, host=C.DEFAULT_SERVER_HOST, port=C.DEFAULT_SERVER_PORT):
        self.__host = host
        self.__port = port

    def send_message(self, message):
        self.__send_message(message, T.REQ_SIMPLE_MESSAGE)

    def __send_message(self, message, type):
        if len(message) > 0:
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((self.__host, self.__port))
                s.settimeout(60)

                message_publisher = MessagePublisher(socket=s, message_and_type=(message, type))
                message_publisher.publish()
            except Exception as e:
                C.LOG.error('Can\'t publish message from client, error : %s' % str(e))

            try:
                message_receiver = MessageReceiver(socket=s, processor=ClientMsgProcessor())
                return message_receiver.receive()
            except soc_error as e:
                C.LOG.error('Couldn\'t get response from server, error : %s' % str(e))
            except Exception as e:
                C.LOG.error("Exception on processing response: {}".format(e))

    def send_file_contents(self, file_path):
        try:
            with open(file_path, 'r') as content_file:
                self.__file_send_routine(content_file.read(), ntpath.basename(file_path))
                content_file.close()
        except IOError as e:
            C.LOG.error('Couldn\'t open file: {}'.format(e.message))

    def __file_send_routine(self, content, file_name):
        size = sys.getsizeof(content)
        msg, type = self.__send_message("{}{}{}".format(file_name, C.DELI, size), T.REQ_FILE_NAME_OK)

        if type == T.RESP_OK:
            self.__send_message("{}{}{}".format(file_name, C.DELI, content), T.REQ_UPLOAD_FILE)
            C.LOG.info("File successfully uploaded to server!")
        else:
            C.LOG.warning(msg)

    def list_all_files(self):
        msg, type = self.__send_message(" ", T.REQ_ALL_FILE_NAMES)

        if type == T.RESP_OK:
            C.LOG.info("All files on server: {}".format(msg))
        else:
            C.LOG.warning(msg)

    def download_file(self, file_name):
        msg, type = self.__send_message(file_name, T.REQ_FILE_DOWNLOAD)

        if type == T.RESP_OK:
            C.LOG.info("File downloaded successfully")
        else:
            C.LOG.warning(msg)