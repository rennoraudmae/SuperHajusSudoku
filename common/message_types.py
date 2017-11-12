REQ_SIMPLE_MESSAGE = '1'
REQ_UPLOAD_FILE = '2'
REQ_ALL_FILE_NAMES = '3'
REQ_FILE_NAME_OK = '4'
REQ_FILE_DOWNLOAD = '5'

RESP_OK = 'a'
RESP_VOID = 'b'
RESP_ERR = 'c'


'''
Here are defined all message types that can be sent and/or received with their functions.
The functions are implemented in corresponding msg_processor classes.
'''
MSG_TYPES = {REQ_SIMPLE_MESSAGE: 'simple_message',
             REQ_UPLOAD_FILE: 'upload_file',
             REQ_ALL_FILE_NAMES: 'req_all_file_names',
             REQ_FILE_NAME_OK: 'file_name_ok',
             REQ_FILE_DOWNLOAD: 'download',
             #
             RESP_OK: 'success',
             RESP_VOID: 'void',
             RESP_ERR: 'error'
             }
