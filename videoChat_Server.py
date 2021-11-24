import socket, cv2, pickle, struct, time
from cv2 import VideoCapture
from cv2 import waitKey

port = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
host_ip = socket.gethostbyname(host)
host_name = socket.gethostbyaddr(host_ip)
full_host = f'{host_ip}:{port}'

print(f'[+] HOST: {host_ip}')
print(f'[+] HOST IP: {host}')
print(f'[+] port: {host_name}')
print(f'[+] HOST name: {host_name}')

server_socket.bind((host_ip, port))
server_socket.listen(5)
starttime = time.time()
cstart = time.ctime(starttime)
print(f'[+] Listening on [{full_host}]\n[{cstart}]')
print('X'*50,'\n')
try:
    while True:
        client_socket, addr = server_socket.accept()
        print(f'[+] Received Connection  [{full_host}]\n[{cstart}]')
        if client_socket:
            vid = cv2.VideoCapture(0)
            while(vid.isOpened()):
                img, frame = vid.read()
                a = pickle.dumps(frame)
                message = struct.pack('Q', len(a))+a
                key = cv2.waitKey(1) & 0xFF
                if key==ord('q'):
                    client_socket.close()


except struct.error as sterror:
    print(sterror)

except Exception as E:
    print(E)








