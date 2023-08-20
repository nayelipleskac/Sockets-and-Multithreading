#Server
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
from pprint import pprint
import random, time

#multithreading imports
import threading, time, random, string
from threading import Thread, active_count, current_thread
from datetime import datetime

connections = {} #keys as username and value as client's socket obj
# red = (255,0,0)
# green =(0,128,0)
# blue = (0,0,255)
# purple = (128,0,128)
# cyan = (0, 255, 255)
# orange = (255,165,0)
conn_list = []

def create_thread(target, args=None):
    t= Thread(target=target, args=args)
    t.daemon = True
    t.start()

class ChatRoom(socket.socket):
    def __init__(self, host = 'localhost', port = 1234):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = host
        self.port = port
        self.bind((self.host, self.port))
        self.listen(10) 

    def start(self): #continuously accepts new conn
        while True: 
            print('start function')
            conn, addr = self.accept()  
            print('Got a connection from ', addr)
            create_thread(self.addUser, args=(conn, addr))
            # print('DICTIONARY: ',connections)
            # print('CONN LIST: ', conn_list)

    def addUser(self, conn, addr):
        print('client connection: ', conn, 'and address: ', addr)
        username = conn.recv(1024).decode('utf-8')
        conn_list.append(username)
        connections[username] = conn
        pprint(connections, indent=4)

        # randomColor =random.choice(colors)
        # socket_colors[conn] = randomColor
        # pprint(socket_colors, indent = 4)
        # self.send_color(randomColor)
        self.listener(username, conn)

    def send_everyone(self, message, source_conn):
        for clientObj in connections.values():
            if clientObj != source_conn: #skip the client that sent the message
                clientObj.send(message.encode())
       

    def listener(self, username, conn):
        while True:
            try: 
                message = conn.recv(1024).decode('utf-8')
                self.send_everyone(('<' + username + '>: ' + message), conn)
            except:  
                self.send_everyone((username + ' has left the chat'), conn)
                del connections[username]
                return #ending the thread 
            
    # def send_color(self, color):
    #     for clientObj in socket_colors.keys():
    #         clientObj.send(color.encode())



if __name__ == '__main__':
    server = ChatRoom('127.0.0.1', 1234)
    server.start()
    
        
