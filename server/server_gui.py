from Tkinter import *
import common.constants as C
from server.tcp_server import TcpServer

'''
Here is defined server GUI
'''

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.server = None
        self.pack()
        self.host_input = None
        self.port_input = None
        self.files_input = None
        self.create_widgets()

    def start_server(self):
        host = self.host_input.get()
        port = int(self.port_input.get())
        self.server = TcpServer(server_inet_addr=host, server_port=port)
        self.server.start_server()

    def stop_server(self):
        if self.server != None:
            self.server.stop_server()
        self.quit()

    def create_widgets(self):
        QUIT = Button(self)
        QUIT["text"] = "QUIT"
        QUIT["fg"] = "red"
        QUIT["command"] = self.stop_server
        QUIT.grid(row=3, column=1)

        Label(self, text="Server port").grid(row=0)
        self.port_input = Entry(self)
        self.port_input.insert(0, str(C.DEFAULT_SERVER_PORT))
        self.port_input.grid(row=0, column=1)

        Label(self, text="Server host").grid(row=1)
        self.host_input = Entry(self)
        self.host_input.insert(0, str(C.DEFAULT_SERVER_HOST))
        self.host_input.grid(row=1, column=1)

        #Label(self, text="File output folder").grid(row=2)
        #self.files_input = Entry(self)
       # self.files_input.insert(0, "files")
        #self.files_input.grid(row=2, column=1)

        start_server = Button(self)
        start_server["text"] = "Start server"
        start_server["command"] = self.start_server
        start_server.grid(row=3, column=0)
