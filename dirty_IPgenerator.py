import socket, sys
from datetime import date


class Dirty_IPgen():
    def __init__(self):
        super(Dirty_IPgen).__init__()
        self.host = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host)

    def IPgen(self):
        print(f'[+] Host-name : \n{self.host}')
        print(f'[+] Host-IP  : \n{self.host_ip}')
        print('[+] Enter Desired IP ')
        ip = input('* ')
        ip_parts = ip.split('.')

        print('[+] Enter Start IP ')
        start = input('* ')
        print('[+] Enter End IP ')
        end = input('* ')

        for x in range(int(start), int(end) + 1):
            NEW_IP = ip_parts[0] + ip_parts[1] + ip_parts[-2] + str(x)
            print(ip_parts[0] + ip_parts[1] + ip_parts[-2] + str(x))
            txt = 'generated_ip.txt'
            generated_ip = str(date.today()) + str(time.ctime()) + str(txt)
            with open(generated_ip, 'a') as f:
                f.write(f'{NEW_IP} \n')
            if x == len(end):
                print(f'[+] Generation Complete, IP\'s are saved: \n [FILENAME] [{generated_ip}.txt')
                # sys.exit(1)


def run_IPgen():
    print('[+]--DIRTY-IP-GENERATOR--[+]')
    Dirty_IPgen()
    Dirty_IPgen().IPgen()

run_IPgen()
