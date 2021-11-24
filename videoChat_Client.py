
import socket, cv2, pickle, struct, time
# brew install imagesnap
# pip3 install sounddevice
# pip3 install cv2
# pip install vext


IP = input('')
PORT = 9999
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))

data = b""
payload_size = struct.calcsize("Q") #Q = long long int (8byte)

while True:
    while len(data) < payload_size:
        packet = clientSocket.recv(4 * 1024) # 4k -- sets up the buffer
        if not packet:
            break
        data += packet
        packed_msg_size = data[:payload_size] #
        print(f'[+] Packed Msg Size: [{packed_msg_size}]')
        data = data[payload_size:] # contains video frame .. replace the size with the frame
        msg_size = struct.unpack('Q', packed_msg_size)[0]
        print(f'[+]  Msg Size:  [{msg_size}]')

        while len(data) < msg_size:
            data += clientSocket.recv(4 *1024)

        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data) ## display output
        cv2.imshow('[+] Received', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

clientSocket.close()




