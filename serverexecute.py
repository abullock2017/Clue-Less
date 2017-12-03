# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# import sockets
#!/usr/bin/python           # This is client.py file

from _thread import *
import threading
from servernet import ServerNet


port = 12346 #Don't change, unless we change on clients, and server router & firewall
# Reserve a port for your service. Will use port 12346 for our game
# Must ensure this port is forwarded on router to PC acting as server computer
# Also, must enable this port on firewall
    
if __name__ == "__main__":
    startsocket = ServerNet(port)   #Instantiate server class
    #Create thread for server listening, not sure if best method, but works.
    #New concept to me, different approach than with VB
    threading.Thread(target = startsocket.listen).start() #Server is now listening for connection requests
    
    #This is a loop for server user to keep entering message. For our clueless
    #Game, we'll just call this function/method as required. 
    while True:
        massmsg = input("MSG to all clients: ")   # Need to verify valid IP address?
        startsocket.sendmsgtoclients(massmsg)
    





