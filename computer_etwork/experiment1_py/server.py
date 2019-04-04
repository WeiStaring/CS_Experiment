from socket import *

# 创建套接字
serverSocket = socket(AF_INET, SOCK_STREAM)
# 绑定端口
serverSocket.bind(("", 8899))
# 监听事件
serverSocket.listen(5)
while True:
    # 接收请求
    clientSocket, clientInfo = serverSocket.accept()
    while True:
        recvData = clientSocket.recv(1024)
        if len(recvData)>0:
            print("%s:%s" %(str(clientInfo), recvData))
        else:
            break

        sendData = input('send:')
        clientSocket.send(bytes(sendData))
    # 关闭套接字
    clientSocket.close()
