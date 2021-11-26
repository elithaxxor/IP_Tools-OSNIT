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



        
        # Part 01 using opencv access webcam and transmit the video in HTML
import cv2
import pyshine as ps  # pip3 install pyshine==0.0.9

HTML = """
<html>
<head>
<title>PyShine Live Streaming</title>
</head>

<body>
<center><h1> PyShine Live Streaming using OpenCV </h1></center>
<center><img src="stream.mjpg" width='640' height='480' autoplay playsinline></center>
</body>
</html>
"""


def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps, HTML)
    address = ('192.168.1.1', 9000)  # Enter your IP address
    try:
        StreamProps.set_Mode(StreamProps, 'cv2'); capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_BUFFERSIZE, 4); capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320); capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        capture.set(cv2.CAP_PROP_FPS, 30); StreamProps.set_Capture(StreamProps, capture); StreamProps.set_Quality(StreamProps, 90)
        server = ps.Streamer(address, StreamProps); print('Server started at', 'http://' + address[0] + ':' + str(address[1]))
        server.serve_forever()
    except KeyboardInterrupt:
        capture.release(); server.socket.close()
if __name__ == '__main__':
    main()
