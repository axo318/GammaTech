import socket
import threading
import time

class Communicator:
    def __init__(self):
        self.currentCommand = None
        self.host = "192.168.105.102"
        self.port = 9999
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))

        self.on = True

    def listen(self):
        self.sock.listen(5)
        threading.Thread(target = self.listenForNextCommand, args=()).start()

    def listenForNextCommand(self):
        while self.on:
            conn, addr = self.sock.accept()
            data = conn.recv(1024)
            extracted = (str(data))[1:]
            finalCommand = extracted.replace("'", "")
            self.currentCommand = finalCommand

    def getCurrentCommand(self):
        #If there is a command, then make sure to delete it before return
        if(self.currentCommand != None):
            temp = self.currentCommand
            self.currentCommand = None
            return temp
        else:
            return None

######### --FOR TESTING-- ##########
# if __name__ == "__main__":
#     com = Communicator()
#     com.listen()
#
#     # Simulates loop in main
#     while(1):
#         command = com.getCurrentCommand()
#         print(command)
#         time.sleep(2)
