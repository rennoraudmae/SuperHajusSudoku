from Tkinter import *
import common.constants as C
from client.tcp_client import TcpClient

'''
Here is defined client GUI.
'''

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.client = None
        self.pack()
        self.host_input = None
        self.port_input = None
        self.files_input = None
        self.create_widgets()
        self.host = None
        self.port = None

    def connect_to_server(self):
        self.host = self.host_input.get()
        self.port = int(self.port_input.get())

        if self.host is None:
            C.LOG.info("No host specified")
            return

        if self.port is None:
            C.LOG.info("No port specified")
            return

        self.client = TcpClient(host=self.host, port=self.port)

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

        Label(self, text="File path").grid(row=2)
        self.files_input = Entry(self)
        self.files_input.insert(0, "test_file.txt")
        self.files_input.grid(row=2, column=1)

        send_file = Button(self)
        send_file["text"] = "CONNECT TO SERVER",
        send_file["command"] = self.connect_to_server
        send_file.grid(row=3, column=0)

        send_file = Button(self)
        send_file["text"] = "PING",
        send_file["command"] = self.ping
        send_file.grid(row=4, column=0)
