import threading
import common.constants as C
from common.message_receiver import MessageReceiver
from common.message_publisher import MessagePublisher
from server.server_msg_processor import ServerMsgProcessor

'''
This is a class, that handles single client processes on server side.
It runs in it's own thread. Every client, that connets, has it's own thread.
'''
class SingleClientHandler(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):

        super(SingleClientHandler, self).__init__(group=group, target=target,
                                                  name=name, verbose=verbose)
        self.kwargs = kwargs
        self.__source = self.kwargs['source']
        self.__processor = ServerMsgProcessor()
        self.__client_socket = self.kwargs['client_socket']
        self.__running = True
        self.__message_handler = MessageReceiver(socket=self.__client_socket, processor=self.__processor)
        self.__message_publisher = MessagePublisher(socket=self.__client_socket)

        C.LOG.debug('New client connected from')
        print self.__source

    def run(self):
        while self.__running:
            response_to_send = self.__message_handler.receive()

            C.LOG.debug("Sending back to client: {}".format(response_to_send))
            self.__message_publisher.publish(response_to_send)

    def stop(self):
        self.__message_handler.stop()
        self.__running = False
        self.__disconnect_client()

    def __disconnect_client(self):
        try:
            self.__client_socket.fileno()
            C.LOG.debug('Closing client socket')
            self.__client_socket.close()
            C.LOG.info('Disconnected client')
        except Exception:
            C.LOG.debug('Socket closed already ...')
            return
        finally:
            self.__client_socket = None
