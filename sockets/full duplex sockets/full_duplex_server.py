#server
#socket imports
import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *
from threading import Thread

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#multithreading imports
import threading, time, random, string
from threading import Thread, active_count, current_thread
from datetime import datetime

def create_thread(target):
    t= Thread(target=target)
    t.daemon = True
    t.start()

class Game(socket.socket, Tk):
    def __init__(self, host = 'localhost', port = 1234):
        Tk.__init__(self)
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)

        self.title('Full Duplex Messaging App: Server')
        self.geometry('400x400')
        self.top_frame = Frame(self)
        self.text_area = Text(self.top_frame, height =  20, width = 50)
        self.bottom_frame= Frame(self)
        self.entry = Entry(self.bottom_frame, width= 40)
        self.send_button = Button(self.bottom_frame, text = 'Send', command = self.send_message)
        
        self.host = host
        self.port = port
        self.conn = None
        self.bind((self.host, self.port))
        self.listen(5)
    def start(self):
        self.conn, addr = self.accept()  #accept connection 
        print('Got a connecton from ', addr)
        print('Got a connecton from ', addr)
        self.pack_components()
    
    def pack_components(self):
        self.top_frame.pack(pady=10)
        self.text_area.pack(side = LEFT, padx= 10)
        self.text_area.tag_configure('right_align', justify='right', foreground = 'red')
        self.text_area.tag_configure('left_align', justify = 'left', foreground='blue')
        self.bottom_frame.pack(pady=10)
        self.entry.pack(padx= 10, side=LEFT)
        self.send_button.pack(side= LEFT)

    def send_message(self): #server is blue, client is red
        message = self.entry.get()
        current_time = datetime.now().strftime('%H:%M:%S')
        print(current_time)
        self.text_area.insert(END, message + ' : ' + current_time + '\n', 'right_align')
        self.entry.delete(0, END)
        self.conn.send(message.encode())
        create_thread(self.accept_message)

    def accept_message(self):
        while True:
            data = self.conn.recv(1024).decode('utf-8')
            print('Received from client: ', data)
            current_time = datetime.now().strftime('%H:%M:%S')
            print(current_time)
            self.text_area.insert(END, data + ' : ' + current_time + '\n', 'left_align')

if __name__ == '__main__':  
    game = Game('127.0.0.1', 1234)
    game.start()
    game.mainloop()








           

