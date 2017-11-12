import common.constants as C
from socket import SHUT_WR, SHUT_RD
import re


class MessageReceiver():
    def __init__(self, socket, processor):
        self.__socket = socket
        self.__message = ""
        self.__processor = processor

    def receive(self):
        terminate = False
        while 1:
            block = self.__socket.recv(C.TCP_RECEIVE_BUFFER_SIZE)
            if block.endswith(C.MESSAGE_TERMINATOR):
                block = block[:-len(C.MESSAGE_TERMINATOR)]
                terminate = True

            if (len(self.__message) + len(block)) >= C.MAX_PDU_SIZE:
                self.__socket.shutdown(SHUT_RD)
                del self.__message
                raise Exception("Remote end-point tried to exceed the MAX_PDU_SIZE ({})".format(C.MAX_PDU_SIZE))

            self.__message += block

            if terminate:
                break

        return self.__processor.process_message(self.get_message())

    def get_message(self):
        if len(self.__message) <= 2:
            raise Exception("Unexpected message from remote system: {}".format(self.__message))
        return self.__message
