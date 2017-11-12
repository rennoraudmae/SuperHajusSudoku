from common.message_processor import MessageProcessor
import common.constants as C

'''
This is client side message processor implementation, which processes only client specific messages and operations.
'''


class ClientMsgProcessor(object, MessageProcessor):
    def __init__(self):
        super(ClientMsgProcessor, self).__init__()

    def ping(self):
        return self.success()
