from socket import *

PORT = 9000
def webServer()
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.bind(('localhost', PORT))
        serverSocket.listen(5)
        while(1):
            (client_socket,address) = serverSocket.accept()
            client_sent = clientsocket.recv(5000).decode()
            pieces =client_sent.split('\n')
            if (len(piece) > 0):
                print(pieces)
            # data = "1.1200 OK\r\n"
            # data += "Content-Type: text/html; charset=utf-8
            # data += '\r\n'
            data = f"1.1200 OK\r\n" + f"Content-Type: text/html; charset=utf-8\r\n" + f'\r\n'
            client_socket.sendall(data.encode())
            client_socket.sutdown(SHUT_WR)

    except KeyboardInterrupt as e:
        print('[+] End-User initiated shutdown.')
    except Exception as e:
        print(str(e))


