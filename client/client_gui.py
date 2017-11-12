from Tkinter import *
import common.constants as C
from client.tcp_client import TcpClient

'''
Here is defined client GUI.
'''


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.host_input = None
        self.port_input = None
        self.user_input = None
        #
        self.client = None
        self.pack()
        self.create_widgets()
        self.host = None
        self.port = None
        self.username = None

    def connect_to_server(self):
        self.host = self.host_input.get()
        self.port = int(self.port_input.get())

        print self.host is None

        if self.host is None:
            self.show_info("Error: no server host specified")
            return

        if self.port is None:
            self.show_info("Error: no server port specified")
            return

        if not self.check_username():
            self.show_info(
                "Error: username not valid. It should containt only alphanumeric characters and must not be longer than 8 characters.")
            return

        self.client = TcpClient(host=self.host, port=self.port)
        if self.client.is_connected():
            self.show_info("Connected to server!")
        else:
            self.show_info("Error: connecting to server failed!")

    def check_username(self):
        self.username = self.user_input.get()

        if not re.match('^[a-zA-Z0-9_]+$', self.username) or len(self.username) > 8:
            return False

        return True

    def ping(self):
        self.client.send_message(message="PING")

    def create_widgets(self):
        QUIT = Button(self)
        QUIT["text"] = "QUIT"
        QUIT["fg"] = "red"
        QUIT["command"] = self.quit
        QUIT.grid(row=3, column=1)

        Label(self, text="Server port").grid(row=0)
        self.port_input = Entry(self)
        self.port_input.insert(0, str(C.DEFAULT_SERVER_PORT))
        self.port_input.grid(row=0, column=1)

        Label(self, text="Server host").grid(row=1)
        self.host_input = Entry(self)
        self.host_input.insert(0, str(C.DEFAULT_SERVER_HOST))
        self.host_input.grid(row=1, column=1)

        Label(self, text="Username").grid(row=2)
        self.user_input = Entry(self)
        self.user_input.insert(0, "(insert user name)")
        self.user_input.grid(row=2, column=1)

        send_file = Button(self)
        send_file["text"] = "CONNECT TO SERVER",
        send_file["command"] = self.connect_to_server
        send_file.grid(row=3, column=0)

        send_file = Button(self)
        send_file["text"] = "PING",
        send_file["command"] = self.ping
        send_file.grid(row=4, column=0)

    def show_info(self, info_msg):
        C.LOG.info(info_msg)
