# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket
from _thread import *
import threading

class ClientNet(object):

    clntsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress
        self.port = 12346  # this is static since we are FWDing to this port
        
        try:
            self.clntsock.connect((ipaddress, self.port))
            #print("Hello, client connect requested")
            threading.Thread(target = self.listen).start()
            
        except:
            print('Error connecting to server')
            self.clntsock.close()
            return False
        
    def sendmsg(self, outMSG):
        encodedMSG = outMSG
        self.clntsock.send(encodedMSG.encode())

    def listen(self):
        # Messages: 1) Move; 2) Suggest; 3) Accuse; 4) Ask to show card; 5) Display show card
        
        while True:
            try:
                incomingMSG = self.clntsock.recv(1024).decode()
                print(incomingMSG, " received from ", self.ipaddress)
                #Here we print the message received, in clueless game, we can
                #Call method in client or server and send message
                
                if incomingMSG[0] == '1':
                    # Here I should client move method. 
                    print('Move player# ', incomingMSG[1], 'in ', incomingMSG[2], ' direction.')
            except:
                print('Lost connection to server')
                self.clntsock.close()
                return False
        self.clntsock.close()

    def clientmove(self, player, direction):
        encodeMSG = "1", player, direction
        sendmsg(encodeMSG)
        
    def clientsuggest(self, player, person, weapon, room):
        encodeMSG = "2", player, person, weapon, room
        sendmsg(encodeMSG)
        
    def clientaccuse(self, player, person, weapon, room):
        encodeMSG = "3", player, person, weapon, room
        sendmsg(encodeMSG)