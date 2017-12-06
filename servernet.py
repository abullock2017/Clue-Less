# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
from _thread import *
import threading
from PyQt5 import QtWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import *
from GameBoard import Ui_GameBoard

class ServerNet(QWidget, Ui_GameBoard):

    svrsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    clients = set()
    clients_lock = threading.Lock()

    def __init__(self, port, playerName):
        self.host = socket.gethostname() # Get local machine name
        self.ip = socket.gethostbyname(self.host)
        self.port = port             # Reserve a port for your service.
        self.svrsock.bind((self.ip, self.port))        # Bind to the port
        QMainWindow.__init__(self)
        self.board = Ui_GameBoard()
        self.board.setupUi(self)
        self.playerName = playerName
        self.board.playerOneNameSlot.setText(self.playerName)

    def listen(self):
        self.svrsock.listen(6)                 # Now wait for client connection.
        #print("Server socket is listening")
        
        while True:
            clnt, addr = self.svrsock.accept()     # Establish connection with client.
            threading.Thread(target = self.listentoclient, args = (clnt, addr)).start() #Start a new thread for each client
        self.svrsock.close()
    
    
    def listentoclient(self, client,address): #This is actioned for each client connection
        with self.clients_lock:
            self.clients.add(client)
        
        while True:
            try:
                msg = (client.recv(1024).decode())  #message received from client

		if msg[0:5] == "Join":
		    self.newPlayerJoin(msg)

                if msg[1:6] == "Char":
		    self.selectCharacter(msg)
                    

                #print(msg, ' received from ', address)
                #This echos client message back to client (only sender), and is client action driven
                #client.send(msg) 
            
            except:
                client.close()
                return False
        client.close() 

    def selectCharacter(self, msg):
	playerNumber = msg[0]
	character = msg[6:]

	'''Assign character to player, send all to clients'''


    def newPlayerJoin(self, msg):

	name = msg[4:]

	if self.board.playerTwoNameSlot.text() == "Waiting...":
            self.board.playerTwoNameSlot.setText( name )
	elif self.board.playerThreeNameSlot.text() == "Waiting...":
	    self.board.playerThreeNameSlot.setText( name )
	elif self.board.playerFourNameSlot.text() == "Waiting...":
	    self.board.playerFourNameSlot.setText( name )
	elif self.board.playerFiveNameSlot.text() == "Waiting...":
	    self.board.playerFiveNameSlot.setText( name )
	elif self.board.playerSixNameSlot.text() == "Waiting...":
	    self.board.playerSixNameSlot.setText( name ) 
	
	players = "Join" + self.board.playerOneNameSlot.text() + "," + self.board.playerTwoNameSlot.text() + "," self.board.playerThreeNameSlot.text() + "," self.board.playerFourNameSlot.text() + "," self.board.playerFiveNameSlot.text() + "," self.board.playerSixNameSlot.text()
	self.sendmsg( players )

	'''NEEDS TO UPDATE BACKEND!!!'''
	
        
    def closeEvent(self, *args, **kwargs):
        #self.svrsocket.close()
        return QWidget.closeEvent(self, *args, **kwargs)
    
    #This sends message to all clients, and is server driven
    def sendmsgtoclients(self, msg):
        with self.clients_lock:
            for clt in self.clients:
                clt.sendall(msg)