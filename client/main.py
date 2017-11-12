from Tkinter import *
from client.client_gui import Application


def main():
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()


if __name__ == "__main__":
    main()
