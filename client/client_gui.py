from Tkinter import *
import common.constants as C
from client.tcp_client import TcpClient


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.client = None
        self.pack()
        self.host_input = None
        self.port_input = None
        self.files_input = None
        self.create_widgets()

    def send_file(self):
        host = self.host_input.get()
        port = int(self.port_input.get())
        self.client = TcpClient(host=host, port=port)
        self.client.send_file_contents(file_path=self.files_input.get())

    def list_files(self):
        host = self.host_input.get()
        port = int(self.port_input.get())
        self.client = TcpClient(host=host, port=port)
        self.client.list_all_files()

    def download_file(self):
        host = self.host_input.get()
        port = int(self.port_input.get())
        self.client = TcpClient(host=host, port=port)
        self.client.download_file(self.files_input.get())

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
        send_file["text"] = "SEND FILE",
        send_file["command"] = self.send_file
        send_file.grid(row=3, column=0)

        list_files = Button(self)
        list_files["text"] = "LIST FILES",
        list_files["command"] = self.list_files
        list_files.grid(row=4, column=0)

        download_file = Button(self)
        download_file["text"] = "DOWNLOAD FILE",
        download_file["command"] = self.download_file
        download_file.grid(row=4, column=1)

