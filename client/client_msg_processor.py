from common.message_processor import MessageProcessor
import common.constants as C


class ClientMsgProcessor(object, MessageProcessor):
    def __init__(self):
        super(ClientMsgProcessor, self).__init__()

    def upload_file(self): #from server
        file_name, file_contents = self._message.split(C.DELI)
        file = open(file_name, "w")
        file.write(file_contents)
        file.close()
        return self.success()