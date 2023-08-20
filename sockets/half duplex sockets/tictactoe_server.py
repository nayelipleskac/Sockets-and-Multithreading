import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *
from threading import Thread

def create_thread(target):
    t = Thread(target=target) #argument - target function
    t.daemon = True
    t.start() 

class Server(socket.socket):
    def __init__(self, host = 'localhost', port = 1234):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port= port
        self.screen = None
        self.board= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

        self.p = 'x'
        self.running = True
        self.conn = None
        self.pos = None
        self.turn = False

        self.bind((self.host, self.port))
        self.listen(5)

    def showtext(self,msg,x,y):
        font= pygame.font.SysFont("freesans" ,32)
        msgobj = font.render(msg,False,(255,0,0))
        self.screen.blit(msgobj,(x,y))

    def start(self):
        self.conn, addr = self.accept()  #accept connection 
        print('Got a connecton from ', addr)
        self.turn = True #server's turn now
        
        self.play()
        print('Got a connecton from ', addr)
        self.conn.send('thank you for connecting '.encode())
    def play(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tic-Tac-Toe server")
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)
     
        print('server: set up game board')
        print('SERVER STARTS FIRST')
        while self.running:
            create_thread(self.accept_message)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1 and self.turn ==True:
                    self.pos = event.pos
                    create_thread(self.send_message)

    def accept_message(self):
        while True:
            data = self.conn.recv(1024).decode()
            if not data:
                break
            print('Received', data)
            x,y = data.split(',',1)
            self.drawO(int(x),int(y))
            self.boxes(int(x),int(y),'o')
            self.turn = True
            self.winner()
            break
    def send_message(self):
        x,y= self.pos
        print('x: {}, y: {}'.format(x,y))
        self.conn.send('{}, {}'.format(x,y).encode())
        self.drawX(x,y)
        self.boxes(x,y,'x')
        print('drawing O in erver')
        self.turn = False   
        print('server just played, client\'s turn')  
        self.winner()                 
       
    def drawX(self,x,y):  
        pygame.draw.line(self.screen,(255,255,255),(x-50,y-50),(x+50,y+50),1) 
        pygame.draw.line(self.screen,(255,255,255),(x+50,y-50),(x-50,y+50),1)
    def drawO(self,x,y):
        pygame.draw.circle(self.screen,(255,255,255),(x,y),70,1) 
    def boxes(self, x, y, player):
        if x in range(0,200) and y in range(0,200): #box 1
            self.update_board(1, player)
        elif x in range(200,400) and y in range(0,200): #box 2
            self.update_board(2, player)
        elif x in range(400,600) and y in range(0,200): #box 3
            self.update_board(3, player)
        elif x in range(0,200) and y in range(200,400): #box 4
            self.update_board(4,player)
        elif x in range(200,400) and y in range(200,400): #box 5
            self.update_board(5, player)
        elif x in range(400,600) and y in range(200,400): #box 6
            self.update_board(6, player)
        elif x in range(0,200) and y in range(400,600): #box 7
            self.update_board(7, player)
        elif x in range(200,400) and y in range(400,600): #box 8
            self.update_board(8, player)
        elif x in range(400,600) and y in range(400,600): #box 9
            self.update_board(9, player)
    def displayWinner(self, n1, n2, n3, player):
        if self.board[n1]==player and self.board[n2]== player and self.board[n3] == player:
            self.printWinner(player)
    def winner(self):
        self.displayWinner(1,2,3,'x')
        self.displayWinner(1,2,3,'o')
        self.displayWinner(4,5,6,'x')
        self.displayWinner(4,5,6,'o')
        self.displayWinner(7,8,9,'x')
        self.displayWinner(7,8,9,'o')
        self.displayWinner(1,5,9,'x')
        self.displayWinner(1,5,9,'o')
        self.displayWinner(7,5,3, 'x')
        self.displayWinner(7,5,3, 'o')
        self.displayWinner(2,5,8, 'x')
        self.displayWinner(2,5,8, 'o')
        self.displayWinner(1,4,7, 'x')
        self.displayWinner(1,4,7, 'o')
        self.displayWinner(3,6,9, 'x')
        self.displayWinner(3,6,9, 'o')
        if (' ' not in self.board.values()):
            print('tie!')
            self.showtext('IT\'S A TIE!', 220, 20)
            pygame.quit()
            self.close()
    
    def update_board(self,pos, val):
        self.board[pos] = val
        print('server: ', self.board)

    def printWinner(self,indicator):
        print('PLAYER {} WINS'.format(indicator))
        self.showtext('PLAYER {} WINS'.format(indicator), 200,20)
        pygame.display.update()
        print('closing server socket conn')
        pygame.quit()
        self.close()
        
if __name__ == '__main__':
    server = Server('127.0.0.1', 1234)
    server.start()


