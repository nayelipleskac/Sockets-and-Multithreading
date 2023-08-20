# Client
#socket imports
import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *
from threading import Thread

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import random, time

#multithreading imports
import threading, time, random, string
from threading import Thread, active_count, current_thread
from datetime import datetime

def create_thread(target):
    t= Thread(target=target)
    t.daemon = True
    t.start()

class Client(socket.socket, Tk):
    def __init__(self, host = 'localhost', port = 1234):
        Tk.__init__(self)
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.title('Chat Room: Client')
        self.geometry('500x500')
        self.loginFrame = Frame(self)
        self.loginLabel = Label(self.loginFrame, text = 'Enter your username below')
        self.loginButton = Button(self.loginFrame, command = self.login, text = 'Login')
        self.loginEntry = Entry(self.loginFrame, width = 70)

        self.chatFrame = Frame(self)
        self.chatText = Text(self.chatFrame)
        self.chatEntry = Entry(self.chatFrame, width = 60)
        self.chatSendButton = Button(self.chatFrame, text = 'Send', command = self.send_message)
        self.na = socket.gethostname()
    def start(self):
        self.connect((self.host, self.port))
        self.pack_components()
        create_thread(self.accept_message)
        # create_thread(self.accept_message)

    def pack_components(self):
        self.loginFrame.pack(pady = 10)
        self.loginLabel.pack()
        self.loginEntry.pack(padx =10)
        self.loginButton.pack()
        
    def accept_message(self): #accept from send_everyone in server
        while True:
            data = self.recv(1024).decode('utf-8')
            if not data:
                break
            print('Received from server: ', data)
            current_time = datetime.now().strftime('%H:%M:%S')
            self.chatText.insert('end', data + ' : ' + current_time + '\n', 'left_align')
            print('accept_message function')
    

    def login(self):
        username = self.loginEntry.get()
        print(username)
        self.send(username.encode())
        # self.loginEntry.delete(0, END)
        self.loginFrame.pack_forget()
        self.chatFrame.pack(fill = BOTH, padx = 10)
        self.chatText.pack()
        self.chatText.tag_configure('right_align', justify='right', foreground = 'red')
        self.chatText.tag_configure('left_align', justify = 'left', foreground='blue')
        self.chatEntry.pack()
        self.chatSendButton.pack()
        
    def send_message(self): #send message from client
        username = self.loginEntry.get()
        message = self.chatEntry.get()
        current_time = datetime.now().strftime('%H:%M:%S')
        self.chatText.insert('end', '<'+ username + '>: '+ message + ' : ' + current_time + '\n', 'right_align')
        print('send_message function')
        self.chatEntry.delete(0, END)
        self.send(message.encode())


if __name__ == '__main__':
    client = Client('127.0.0.1', 1234)
    client.start()
    client.mainloop()

