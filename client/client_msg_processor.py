from common.message_processor import MessageProcessor
import common.constants as C


class ClientMsgProcessor(object, MessageProcessor):
    def __init__(self):
        super(ClientMsgProcessor, self).__init__()

    def ping(self):
        return self.success()
