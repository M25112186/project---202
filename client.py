import socket
from threading import Thread
from tkinter import *
from tkinter import font

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300, bg="#7CB9E8")
        
        self.pls = Label(self.login,
                         text="Please login to continue",
                         justify=CENTER,
                         font="Helvetica 14 bold",
                         bg="#7CB9E8",
                         fg="#041E42")
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)

        self.labelName = Label(self.login,
                               text="Name: ",
                               font="Helvetica 12",
                               bg="#7CB9E8",
                               fg="#041E42")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)

        self.entryName = Entry(self.login,
                               font="Helvetica 14",
                               bg="#e3f2fd",
                               fg="#0d47a1",
                               bd=0,
                               highlightthickness=1,
                               highlightbackground="#0d47a1",
                               highlightcolor="#0d47a1")
        self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entryName.focus()

        self.go = Button(self.login,
                         text="CONTINUE",
                         font="Helvetica 14 bold",
                         bg="#6495ED",
                         fg="#041E42",
                         activebackground="#81c784",
                         activeforeground="#041E42",
                         bd=0,
                         command=lambda: self.goAhead(self.entryName.get()))
        self.go.place(relx=0.4, rely=0.55, relwidth=0.3, relheight=0.1)
        self.go.configure(cursor="hand2")

        self.window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.name = name
        rcv = Thread(target=self.receive)
        rcv.start()

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass
            except:
                print("An error occurred!")
                client.close()
                break

g = GUI()
