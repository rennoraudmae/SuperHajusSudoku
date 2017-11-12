from socket import socket, AF_INET, SOCK_STREAM
from socket import error as soc_error, timeout
from threading import Thread
import common.constants as C
from common.message_receiver import MessageReceiver
from server.server_msg_processor import ServerMsgProcessor
from common.message_publisher import MessagePublisher


class TcpServer():
    def __init__(self, server_inet_addr=C.DEFAULT_SERVER_HOST, server_port=C.DEFAULT_SERVER_PORT):
        # constants
        self.SERVER_PORT = server_port
        self.SERVER_INET_ADDR = server_inet_addr
        self.__DEFAULT_SERVER_TCP_CLIENTS_QUEUE = 10
        # member vars
        self.__server_socket = None
        self.__client_socket = None
        self.__running = False
        self.processor = ServerMsgProcessor()
        # init
        self.init_server()

        self.__serving_thread = Thread(target=self.serve_forever)

    def start_server(self):
        self.__running = True
        self.__serving_thread.start()

    def set_files_folder(self, folder):
        self.processor.files_folder = folder

    def init_server(self):
        self.__server_socket = socket(AF_INET, SOCK_STREAM)
        self.__server_socket.settimeout(2)
        C.LOG.debug('Server socket created, descriptor %d' % self.__server_socket.fileno())
        try:
            self.__server_socket.bind((self.SERVER_INET_ADDR, self.SERVER_PORT))
        except soc_error as e:
            C.LOG.error('Can\'t start server, error : %s' % str(e))
            exit(1)

        C.LOG.debug('Server socket bound on %s:%d' % self.__server_socket.getsockname())
        self.__server_socket.listen(self.__DEFAULT_SERVER_TCP_CLIENTS_QUEUE)
        C.LOG.info('Accepting requests on TCP %s:%d' % self.__server_socket.getsockname())

    def serve_forever(self):
        while self.__running:
            try:
                self.__client_socket, source = self.__server_socket.accept()

                C.LOG.debug('New client connected from %s:%d' % source)
                message_handler = MessageReceiver(socket=self.__client_socket, processor=self.processor)
                response_to_send = message_handler.receive()

                C.LOG.debug("Sending back to client: {}".format(response_to_send))
                message_publisher = MessagePublisher(socket=self.__client_socket, message_and_type=response_to_send)
                message_publisher.publish()

                C.LOG.info("Message received...")
                self.__disconnect_client()
            except (timeout):
                C.LOG.info('Awaiting connections...')
            except (soc_error) as e:
                C.LOG.error('Interrupted receiving the data from %s:%d, ' \
                            'error: %s' % (source + (e,)))
                self.__disconnect_client()
                continue

    def stop_server(self):
        self.__running = False
        self.__disconnect_client()
        self.__server_socket.close()
        self.__serving_thread.join()
        C.LOG.info('Server closed')

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
