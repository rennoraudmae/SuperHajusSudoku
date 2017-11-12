class CommunicationException(Exception):
    def __init__(self, message):
        super(CommunicationException, self).__init__(message)
