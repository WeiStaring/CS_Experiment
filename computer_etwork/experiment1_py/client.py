from socket import *

def main():
    # 创建套接
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # 连接
    clientSocket.connect(('127.0.0.1', 8899))

    clientSocket.send('haha'.encode('utf-8'))

    recvData = clientSocket.recv(1024)
    print('recvData:%s' %recvData)

    # 关闭套接字
    clientSocket.close()

if __name__ == "__main__" :
    main()