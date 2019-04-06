import socket,select,threading


class Client:
    def __init__(self):
        self.client_socket = socket.socket()
        self.host = socket.gethostname()
        self.client_addr = (self.host,8899)
        self.client_socket.connect(self.client_addr)
        listen = threading.Thread(target=self.listening)
        listen.start()
        while True:
            try:
                user_input = input(">>>")
            except Exception as e:
                continue
            self.client_socket.send(user_input.encode('utf8'))
            if user_input == 'quit':
                break

    def listening(self):
        inputs = [self.client_socket]
        while True:
            rlist, wlist, elist = select.select(inputs, [], [])
            if self.client_socket in rlist:
                try:
                    print(self.client_socket.recv(1024))
                except socket.error:
                    print("socket break down")
                    exit()

if __name__ == "__main__":
    client = Client()