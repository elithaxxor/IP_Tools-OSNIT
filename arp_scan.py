
##### IMPROVED ARP ##


 import nmap, re, traceback
from typing import Pattern, Match




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
        #sip_add_entered = ip_add_pattern.search(ip_add_entered)
        if ip_add_pattern:
            print(f"{ip_add_entered} is a valid ip address")
            break
    while True:
        print(f"**{yellow}**Enter the port range {reset}\n ")
        global port_range
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

    master_results = []
    nm = nmap.PortScanner()
    for port in range(port_min, port_max + 1):
        try:
            print('X'*50)
            #port_max += 1
            ip_add_entered = str(ip_add_entered)
            port = str(port)
            result = nm.scan(ip_add_entered, str(port))
            print(f'**{yellow}All Dictinary Keys:: {reset} \n{[*result.values()]}') ## unpacks all dictinary keys
            print(result.keys())
            print('X'*50)
            print(f'{yellow}**[TARGET]-- {reset}[{ip_add_entered}]\n{yellow}*[PORT-MIN]{reset}{port_min} \n{yellow}*[PORT-MAX]{reset}{port_max}')
            print('X'*50)

            print(f'{yellow}**[RESULTS]{reset}')
            print(result)
            #print([(k, result[timestr]) for k in result])
            #print(f'{yellow}**[CURRENT-PORT]{reset}\n{result["scaninfo"]}')
            print(f'{yellow}**[CURRENT-PORT]{reset}\n{port}')
            print(f'{yellow}**[SCAN-TIME]{reset}\n{port}')
            print(f'{yellow}**[ELAPSED-TIME]{reset}\n{port}')
            print('X'*50)
            print(list(result.values()))
            master_results.append(result)
            if port == port_max:
                return f'{red}**End of arp scan {master_results}'
        except Exception as e:
            traceback.print_exc()
            print(f"{red}**ERROR IN NMAP SCAN[{port}]{reset}.\n[{e}]")


results = arp_scan()
print('X' * 50)
print(f'{yellow} ARP-SCAN COMPLETE'{reset})
print(results)













############################old ########

def arp_scan():
    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535
    open_ports = []
    # Ask user to input the ip address they want to scan.
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        print(f"**{yellow}**Enter the IP address for scanning  {reset}\n ")
        port_range = input("* ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is a valid ip address")
            break
    while True:
        print(f"**{yellow}**Enter the port range {reset}\n ")
        port_range = input("* ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    nm = nmap.PortScanner()
    for port in range(port_min, port_max + 1):
        try:
            result = nm.scan(ip_add_entered, str(port))
            print(result)
            port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
            print(f"Port {port} is {port_status}")
        except:
            traceback.print_exc()
            print(f"{red}**ERROR IN NMAP SCAN{port}.")
