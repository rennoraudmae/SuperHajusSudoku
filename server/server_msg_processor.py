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

    def upload_file(self):
        C.LOG.info("Writing new file to disc")
        file_name, file_contents = self._message.split(C.DELI)
        full_path = os.path.join(self.files_folder, file_name)
        dirname = os.path.dirname(full_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        file = open(full_path, "w")
        file.write(file_contents)
        file.close()
        return self.success()

    def req_all_file_names(self):
        all_file_names = [f for f in listdir(self.files_folder) if isfile(join(self.files_folder, f))]
        return all_file_names, T.RESP_OK

    def file_name_ok(self):
        file_name, file_size = self._message.split(C.DELI)
        full_path = os.path.join(self.files_folder, file_name)

        folder_current_size = self.__get_folder_size(self.files_folder)
        has_enough_space = (C.MAX_FOLDER_CAPACITY - folder_current_size - int(file_size)) > 0

        if os.path.isfile(full_path):
            return self.__error("File already existing")
        if not has_enough_space:
            return self.__error("Not enough space on disk")
        else:
            return self.success()

    def download(self):
        file_name = self._message
        full_path = os.path.join(self.files_folder, file_name)
        if not os.path.isfile(full_path):
            return self.__error("No such file existing on server")
        else:
            msg = "{}{}{}".format(file_name, C.DELI, self.__get_file_contents(full_path))
            return msg, T.REQ_UPLOAD_FILE

    def __get_file_contents(self, file_path):
        try:
            with open(file_path, 'r') as content_file:
                contents = content_file.read()
                content_file.close()
                return contents
        except IOError as e:
            C.LOG.error('Couldn\'t open file: {}'.format(e.message))

    def __error(self, message):
        return message, T.RESP_ERR

    def __get_folder_size(self, start_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size
