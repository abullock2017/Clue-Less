# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#!/usr/bin/python           # This is client.py file

from clientnet import ClientNet #File clientnet, class is ClientNet

if __name__ == "__main__":
    
    host = input("Please enter IP address: ")   #This get server IP from user
    clientconnection = ClientNet(host)          #Established socket to server
    
    while True:
        message = input("Please enter message to server: ")
        if  (message == 'end'):
            break
        
        #Below code, sends message to server
        #For Clueless game, each user must establish socket as per ClientNet(host) above.
        #And, use below line of code to send to messages to the server.
        clientconnection.sendmsg(message)
        

    
    
    
    
    
    
    





