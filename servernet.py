# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
from _thread import *
import threading

class ServerNet(object):

    svrsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    clients = set()
    clients_lock = threading.Lock()

    def __init__(self, port):
        self.host = socket.gethostname() # Get local machine name
        self.ip = socket.gethostbyname(self.host)
        self.port = port             # Reserve a port for your service.
        self.svrsock.bind((self.ip, self.port))        # Bind to the port

    def listen(self):
        self.svrsock.listen(6)                 # Now wait for client connection.
        #print("Server socket is listening")
        
        while True:
            clnt, addr = self.svrsock.accept()     # Establish connection with client.
            #print ('Connected to: ', addr[0], ': ', addr[1]) #Just prints IP and port of client
            threading.Thread(target = self.listentoclient, args = (clnt, addr)).start() #Start a new thread for each client
        svrsock.close()
    
    def listentoclient(self, client,address): #This is actioned for each client connection
        with self.clients_lock:
            self.clients.add(client)
        
        while True:
            try:
                msg = (client.recv(1024).decode())  #message received from client
                #print(msg, ' received from ', address)
                #This echos client message back to client (only sender), and is client action driven
                client.send(msg.encode()) 
            
            except:
                client.close()
                return False
        client.close() 
        
    #This sends message to all clients, and is server driven
    def sendmsgtoclients(self, msg):
        with self.clients_lock:
            for clt in self.clients:
                clt.sendall(msg.encode())