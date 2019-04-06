from socket import *
import select
import threading


class Server:
    def __init__(self):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(("", 8899))
        self.serverSocket.listen(5)
        self.fd_name = {}  # nickname map
        self.inputs = []   # listen
        self.inputs.append(self.serverSocket)
        print("server is running")

    def new_connect(self):
        clientSocket, clientInfo = self.serverSocket.accept()
        try:
            clientSocket.send(bytes("welcome to chatroom,pls set up your nick name!", encoding='utf8'))
            client_name = clientSocket.recv(1024)
            self.fd_name[clientSocket] = client_name
            self.inputs.append(clientSocket)
            print(client_name, 'enter the room')
            self.forcast(self.fd_name[clientInfo] + bytes("join",encoding='utf8'), clientSocket)
        except Exception as e:
            print(e)

    def run(self):
        while True:
            rlist, wlist, elist = select.select(self.inputs, [], [])
            if not rlist:
                print('out')
                self.serverSocket.close()
                break
            for r in rlist:
                if r is self.serverSocket:
                    self.new_connect()
                else:
                    try:
                        data = r.recv(1024)
                        data = self.fd_name[r] + bytes(":",encoding='utf8') + data
                    except error:
                        data = self.fd_name[r] + bytes("leaved the room",encoding='utf8')
                        print(self.fd_name[r], 'leave the room')
                        self.inputs.remove(r)
                        del self.fd_name[r]
                    self.forcast(data, r)

    def forcast(self, mess, excepts):
        for socket in self.fd_name.keys():
            if socket != excepts and socket != self.serverSocket:
                socket.send(mess)

    def remove(self, r, data):
        self.inputs.remove(r)
        print(data)
        self.forcast(data, r)


def main():
    server = Server()
    server.run()


if __name__ == "__main__":
    main()