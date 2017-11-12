from common.message_processor import MessageProcessor
import common.constants as C
import common.message_types as T
import os.path
from os import listdir
from os.path import isfile, join


class ServerMsgProcessor(object, MessageProcessor):
    def __init__(self):
        super(ServerMsgProcessor, self).__init__()
        self.files_folder = ""

    def ping(self):
        return "", T.RESP_OK

    def __error(self, message):
        return message, T.RESP_ERR
