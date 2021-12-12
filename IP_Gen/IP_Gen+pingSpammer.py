import socket, sys, os
from datetime import datetime
from datetime import date
import time


class Dirty_IPgen():
    def __init__(self):
      #  super().__init__()
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
            self.generated_ip = str(date.today()) + str(time.ctime()) + str(txt)
            global text_loc
            text_loc = self.generated_ip
            with open(self.generated_ip, 'a') as f:
                f.write(f'{NEW_IP} \n')
            if x == len(end):
                print(f'[+] Generation Complete, IP\'s are saved: \n [FILENAME] [{self.generated_ip}.txt')


    class Spam_IP():
        def __init__(self,):
            super().__init__()
            self.self = self

        def run_spam(self):
            ping_log = []
            counter = 0
            print(f'[+] File to read : \n\t\t{os.getcwd()}')
            with open(text_loc) as f:
                dump = f.read()
                dump.splitlines()
                print(len(dump)); print(type(dump))
                for ip in dump:
                    os.system('cls')
                    print('[+] Starting Sequence (2 ping per client) .. ')
                    os.system(f'ping -n 2 {ip}')

                    if ip:
                        print(f'[+] --[Ping Successfull]--  {date.today()} || {time.ctime()} \n[{ip}] ')
                        success_log = f'[+] Success {ip}\n'
                        ping_log.append(success_log + ip)
                        name = 'ping_log.txt'
                        ping_list = str(date.today()) + str(time.ctime()) + str(name)
                        with open(ping_list, 'a') as f:
                            f.write(f'[+] Successful Ping {date.today()} || {time.ctime()} \n[{ip}] \n\n')
                        print(ping_log)
                    elif counter <= len(text_loc):
                        print(f'[-] --[Ping Failed]--  {date.today()} || {time.ctime()} \n[{ip}] ')
                        ping_list = str(date.today()) + str(time.ctime()) + str(name)
                        with open(ping_list, 'a') as f:
                            f.write(f'[+] Successful Ping {date.today()} || {time.ctime()} \n[{ip}] \n\n')
                            f.close()

                    else:
                        print(f'[-] --[Ping Failed]--  {date.today()} || {time.ctime()} \n[{ip}] ')
                        ping_list = str(date.today()) + str(time.ctime()) + str(name)
                        with open(ping_list, 'a') as f:
                            f.write(f'[+] Successful Ping {date.today()} || {time.ctime()} \n[{ip}] \n\n')
                            f.close()


def run_IPgen():
    affirmative =['yes','YES','y','Y']
    affirmative =['yes','YES','y','Y']
    print('[+]--DIRTY-IP-GENERATOR--[+]')
    Dirty_IPgen()
    Dirty_IPgen().IPgen()
    print('[+]--Spam IP\'s with Ping? --[+]')
    ans = input('')
    if ans in affirmative:
        print('[+]-- IP SPAMMER BY LIST--[+]')
        Dirty_IPgen().Spam_IP().run_spam()


       # Spam_IP().run_spam()

        if Dirty_IPgen().Spam_IP():
            print('[+]-- IP/s SPAMMED chec CWD for .txt--[+]')
            sys.exit(1)

run_IPgen()
